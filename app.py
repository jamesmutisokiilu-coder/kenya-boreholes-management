from flask import Flask, render_template, request, send_file, jsonify
from io import BytesIO
from datetime import datetime
import os
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether
)


# ============================================================
# FLASK APPLICATION
# ============================================================

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "kenya-boreholes-services-secret-key"
)


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


# ============================================================
# HEALTH CHECK
# ============================================================

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "application": "Kenya Boreholes Services"
    })


# ============================================================
# ABOUT / SERVICES / CONTACT OPTIONAL ROUTES
# ============================================================

@app.route("/about")
def about():
    return render_template("index.html")


@app.route("/services")
def services():
    return render_template("index.html")


@app.route("/contact")
def contact():
    return render_template("index.html")


# ============================================================
# QUOTATION PDF
# ============================================================

@app.route("/generate-quotation", methods=["POST"])
def generate_quotation():

    try:

        data = request.get_json(silent=True)

        if not data:
            data = request.form.to_dict()

        # ----------------------------------------------------
        # CUSTOMER DETAILS
        # ----------------------------------------------------

        customer_name = str(
            data.get("customerName", "")
        ).strip()

        phone = str(
            data.get("phone", "")
        ).strip()

        email = str(
            data.get("email", "")
        ).strip()

        location = str(
            data.get("location", "")
        ).strip()

        service = str(
            data.get("service", "")
        ).strip()

        capacity = str(
            data.get("capacity", "")
        ).strip()

        project_date = str(
            data.get("projectDate", "")
        ).strip()

        validity = str(
            data.get("validity", "30 Days")
        ).strip()

        notes = str(
            data.get("notes", "")
        ).strip()

        # ----------------------------------------------------
        # EXTRA CHARGES
        # ----------------------------------------------------

        labour = safe_float(
            data.get("labour", 0)
        )

        transport = safe_float(
            data.get("transport", 0)
        )

        # ----------------------------------------------------
        # ITEMS
        # ----------------------------------------------------

        items = data.get("items", [])

        if isinstance(items, str):

            items = []

        cleaned_items = []

        for item in items:

            if not isinstance(item, dict):
                continue

            description = str(
                item.get("description", "")
            ).strip()

            quantity = safe_float(
                item.get("quantity", 0)
            )

            unit_price = safe_float(
                item.get("price", 0)
            )

            amount = quantity * unit_price

            if description:

                cleaned_items.append({
                    "description": description,
                    "quantity": quantity,
                    "price": unit_price,
                    "amount": amount
                })

        # ----------------------------------------------------
        # TOTAL
        # ----------------------------------------------------

        items_total = sum(
            item["amount"]
            for item in cleaned_items
        )

        grand_total = (
            items_total
            + labour
            + transport
        )

        # ----------------------------------------------------
        # QUOTATION NUMBER
        # ----------------------------------------------------

        quotation_number = generate_quotation_number()

        quotation_date = datetime.now().strftime(
            "%d %B %Y"
        )

        # ----------------------------------------------------
        # CREATE PDF IN MEMORY
        # ----------------------------------------------------

        pdf_buffer = BytesIO()

        document = SimpleDocTemplate(

            pdf_buffer,

            pagesize=A4,

            rightMargin=15 * mm,
            leftMargin=15 * mm,
            topMargin=15 * mm,
            bottomMargin=15 * mm,

            title=f"Quotation {quotation_number}",

            author="Kenya Boreholes Services"
        )

        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(

            "Title",

            parent=styles["Heading1"],

            fontName="Helvetica-Bold",

            fontSize=16,

            leading=20,

            alignment=TA_LEFT,

            spaceAfter=4
        )

        subtitle_style = ParagraphStyle(

            "Subtitle",

            parent=styles["Normal"],

            fontName="Helvetica",

            fontSize=9,

            leading=12
        )

        heading_style = ParagraphStyle(

            "Heading",

            parent=styles["Heading2"],

            fontName="Helvetica-Bold",

            fontSize=10,

            leading=13,

            textColor=colors.white,

            spaceBefore=10,

            spaceAfter=6
        )

        normal_style = ParagraphStyle(

            "NormalCustom",

            parent=styles["Normal"],

            fontName="Helvetica",

            fontSize=8.5,

            leading=11
        )

        small_style = ParagraphStyle(

            "Small",

            parent=styles["Normal"],

            fontName="Helvetica",

            fontSize=7.5,

            leading=10
        )

        right_style = ParagraphStyle(

            "Right",

            parent=normal_style,

            alignment=TA_RIGHT
        )

        center_style = ParagraphStyle(

            "Center",

            parent=normal_style,

            alignment=TA_CENTER
        )

        # ----------------------------------------------------
        # PDF CONTENT
        # ----------------------------------------------------

        story = []

        # ----------------------------------------------------
        # COMPANY HEADER
        # ----------------------------------------------------

        company_block = [

            Paragraph(
                "KENYA BOREHOLES SERVICES",
                title_style
            ),

            Paragraph(
                "Professional Water Solutions Across Kenya",
                subtitle_style
            ),

            Spacer(1, 2 * mm),

            Paragraph(
                "Borehole Drilling • Water Testing • Pump Installation • Maintenance • Water Delivery",
                small_style
            )
        ]

        reference_block = [

            Paragraph(
                "<b>QUOTATION</b>",
                ParagraphStyle(
                    "QuoteTitle",
                    parent=styles["Heading2"],
                    fontName="Helvetica-Bold",
                    fontSize=15,
                    alignment=TA_RIGHT
                )
            ),

            Paragraph(
                f"<b>Quotation Ref:</b> {quotation_number}",
                right_style
            ),

            Paragraph(
                f"<b>Date:</b> {quotation_date}",
                right_style
            ),

            Paragraph(
                f"<b>Validity:</b> {validity or '30 Days'}",
                right_style
            )
        ]

        header_table = Table(
            [[company_block, reference_block]],
            colWidths=[
                115 * mm,
                60 * mm
            ]
        )

        header_table.setStyle(

            TableStyle([

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP"
                ),

                (
                    "ALIGN",
                    (1, 0),
                    (1, 0),
                    "RIGHT"
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    8
                ),

                (
                    "LINEBELOW",
                    (0, 0),
                    (-1, 0),
                    1,
                    colors.HexColor("#2b8ef1")
                )

            ])

        )

        story.append(header_table)

        story.append(
            Spacer(1, 5 * mm)
        )

        # ----------------------------------------------------
        # CUSTOMER DETAILS
        # ----------------------------------------------------

        story.append(

            Table(

                [[
                    Paragraph(
                        "CUSTOMER / PROJECT DETAILS",
                        ParagraphStyle(
                            "DetailHeading",
                            parent=normal_style,
                            fontName="Helvetica-Bold",
                            fontSize=9,
                            textColor=colors.white
                        )
                    )
                ]],

                colWidths=[175 * mm],

                style=TableStyle([

                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, -1),
                        colors.HexColor("#2b8ef1")
                    ),

                    (
                        "LEFTPADDING",
                        (0, 0),
                        (-1, -1),
                        6
                    ),

                    (
                        "TOPPADDING",
                        (0, 0),
                        (-1, -1),
                        5
                    ),

                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, -1),
                        5
                    )

                ])

            )

        )

        customer_data = [

            [
                Paragraph("<b>Client</b>", normal_style),
                Paragraph(customer_name or "-", normal_style),

                Paragraph("<b>Phone</b>", normal_style),
                Paragraph(phone or "-", normal_style)
            ],

            [
                Paragraph("<b>Email</b>", normal_style),
                Paragraph(email or "-", normal_style),

                Paragraph("<b>Location</b>", normal_style),
                Paragraph(location or "-", normal_style)
            ],

            [
                Paragraph("<b>Service</b>", normal_style),
                Paragraph(service or "-", normal_style),

                Paragraph("<b>Capacity</b>", normal_style),
                Paragraph(capacity or "-", normal_style)
            ],

            [
                Paragraph("<b>Project Date</b>", normal_style),
                Paragraph(
                    project_date or "-",
                    normal_style
                ),

                Paragraph("<b>Validity</b>", normal_style),
                Paragraph(
                    validity or "30 Days",
                    normal_style
                )
            ]

        ]

        customer_table = Table(

            customer_data,

            colWidths=[
                24 * mm,
                63 * mm,
                24 * mm,
                64 * mm
            ]
        )

        customer_table.setStyle(

            TableStyle([

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.4,
                    colors.HexColor("#d8dee8")
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP"
                ),

                (
                    "BACKGROUND",
                    (0, 0),
                    (0, -1),
                    colors.HexColor("#f5f7fa")
                ),

                (
                    "BACKGROUND",
                    (2, 0),
                    (2, -1),
                    colors.HexColor("#f5f7fa")
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                )

            ])

        )

        story.append(customer_table)

        story.append(
            Spacer(1, 5 * mm)
        )

        # ----------------------------------------------------
        # ITEMS HEADING
        # ----------------------------------------------------

        story.append(

            Table(

                [[
                    Paragraph(
                        "MATERIALS & REQUIREMENTS",
                        ParagraphStyle(
                            "MaterialsHeading",
                            parent=normal_style,
                            fontName="Helvetica-Bold",
                            fontSize=9,
                            textColor=colors.white
                        )
                    )
                ]],

                colWidths=[175 * mm],

                style=TableStyle([

                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, -1),
                        colors.HexColor("#2b8ef1")
                    ),

                    (
                        "LEFTPADDING",
                        (0, 0),
                        (-1, -1),
                        6
                    ),

                    (
                        "TOPPADDING",
                        (0, 0),
                        (-1, -1),
                        5
                    ),

                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, -1),
                        5
                    )

                ])

            )

        )

        # ----------------------------------------------------
        # ITEMS TABLE
        # ----------------------------------------------------

        item_rows = [

            [
                Paragraph(
                    "<b>No.</b>",
                    center_style
                ),

                Paragraph(
                    "<b>Description</b>",
                    normal_style
                ),

                Paragraph(
                    "<b>Quantity</b>",
                    center_style
                ),

                Paragraph(
                    "<b>Unit Price (KES)</b>",
                    right_style
                ),

                Paragraph(
                    "<b>Amount (KES)</b>",
                    right_style
                )
            ]

        ]

        for index, item in enumerate(
            cleaned_items,
            start=1
        ):

            item_rows.append(

                [
                    Paragraph(
                        str(index),
                        center_style
                    ),

                    Paragraph(
                        escape_html(
                            item["description"]
                        ),
                        normal_style
                    ),

                    Paragraph(
                        format_number(
                            item["quantity"]
                        ),
                        center_style
                    ),

                    Paragraph(
                        format_money(
                            item["price"]
                        ),
                        right_style
                    ),

                    Paragraph(
                        format_money(
                            item["amount"]
                        ),
                        right_style
                    )
                ]

            )

        # If no items were supplied

        if not cleaned_items:

            item_rows.append(

                [
                    Paragraph(
                        "1",
                        center_style
                    ),

                    Paragraph(
                        "Borehole / Water Service",
                        normal_style
                    ),

                    Paragraph(
                        "1",
                        center_style
                    ),

                    Paragraph(
                        "0.00",
                        right_style
                    ),

                    Paragraph(
                        "0.00",
                        right_style
                    )
                ]

            )

        item_rows.append(

            [
                "",
                Paragraph(
                    "<b>Labour & Tank/Borehole Servicing</b>",
                    normal_style
                ),
                "",
                "",
                Paragraph(
                    format_money(labour),
                    right_style
                )
            ]

        )

        item_rows.append(

            [
                "",
                Paragraph(
                    "<b>Transport & Logistics</b>",
                    normal_style
                ),
                "",
                "",
                Paragraph(
                    format_money(transport),
                    right_style
                )
            ]

        )

        items_table = Table(

            item_rows,

            colWidths=[
                12 * mm,
                78 * mm,
                22 * mm,
                31 * mm,
                32 * mm
            ],

            repeatRows=1
        )

        items_table.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#eaf2ff")
                ),

                (
                    "TEXTCOLOR",
                    (0, 0),
                    (-1, 0),
                    colors.HexColor("#1d3557")
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.4,
                    colors.HexColor("#ccd3dd")
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                ),

                (
                    "ALIGN",
                    (0, 0),
                    (0, -1),
                    "CENTER"
                ),

                (
                    "ALIGN",
                    (2, 1),
                    (2, -1),
                    "CENTER"
                ),

                (
                    "ALIGN",
                    (3, 1),
                    (-1, -1),
                    "RIGHT"
                ),

                (
                    "SPAN",
                    (0, len(item_rows) - 2),
                    (3, len(item_rows) - 2)
                ),

                (
                    "SPAN",
                    (0, len(item_rows) - 1),
                    (3, len(item_rows) - 1)
                ),

                (
                    "BACKGROUND",
                    (0, len(item_rows) - 2),
                    (-1, len(item_rows) - 1),
                    colors.HexColor("#f7f9fc")
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    5
                )

            ])

        )

        story.append(items_table)

        # ----------------------------------------------------
        # TOTAL
        # ----------------------------------------------------

        story.append(
            Spacer(1, 3 * mm)
        )

        total_table = Table(

            [[
                Paragraph(
                    "<b>TOTAL QUOTATION</b>",
                    ParagraphStyle(
                        "TotalLabel",
                        parent=normal_style,
                        fontName="Helvetica-Bold",
                        fontSize=10,
                        alignment=TA_RIGHT
                    )
                ),

                Paragraph(
                    f"<b>KES {format_money(grand_total)}</b>",
                    ParagraphStyle(
                        "TotalAmount",
                        parent=normal_style,
                        fontName="Helvetica-Bold",
                        fontSize=11,
                        alignment=TA_RIGHT
                    )
                )
            ]],

            colWidths=[
                125 * mm,
                50 * mm
            ]
        )

        total_table.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, -1),
                    colors.HexColor("#eaf2ff")
                ),

                (
                    "BOX",
                    (0, 0),
                    (-1, -1),
                    0.8,
                    colors.HexColor("#2b8ef1")
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    8
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    8
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    7
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    7
                )

            ])

        )

        story.append(total_table)

        # ----------------------------------------------------
        # NOTES
        # ----------------------------------------------------

        story.append(
            Spacer(1, 6 * mm)
        )

        story.append(

            Paragraph(
                "<b>TERMS & NOTES</b>",
                ParagraphStyle(
                    "TermsHeading",
                    parent=normal_style,
                    fontName="Helvetica-Bold",
                    fontSize=10,
                    textColor=colors.HexColor("#1d3557")
                )
            )

        )

        story.append(
            Spacer(1, 2 * mm)
        )

        standard_terms = [

            "Quotation is based on the listed materials and stated project scope.",

            "Any additional repairs or materials required after inspection will be communicated and quoted separately.",

            "Prices are subject to confirmation before commencement of works.",

            "Site assessment may be required before final confirmation.",

            f"This quotation is valid for {validity or '30 Days'}."

        ]

        if notes:

            for note in notes.splitlines():

                note = note.strip()

                if note:

                    standard_terms.append(note)

        for term in standard_terms:

            story.append(

                Paragraph(
                    f"• {escape_html(term)}",
                    small_style
                )

            )

            story.append(
                Spacer(1, 1.2 * mm)
            )

        # ----------------------------------------------------
        # SIGNATURE
        # ----------------------------------------------------

        story.append(
            Spacer(1, 8 * mm)
        )

        signature_table = Table(

            [[

                Paragraph(
                    "<b>KENYA BOREHOLES SERVICES</b><br/>"
                    "Professional Water Solutions Across Kenya",
                    small_style
                ),

                Paragraph(
                    "<b>Authorized By</b><br/><br/>"
                    "____________________________",
                    small_style
                )

            ]],

            colWidths=[
                105 * mm,
                70 * mm
            ]
        )

        signature_table.setStyle(

            TableStyle([

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP"
                ),

                (
                    "ALIGN",
                    (1, 0),
                    (1, 0),
                    "RIGHT"
                )

            ])

        )

        story.append(signature_table)

        # ----------------------------------------------------
        # BUILD PDF
        # ----------------------------------------------------

        document.build(story)

        pdf_buffer.seek(0)

        safe_customer_name = clean_filename(
            customer_name or "Customer"
        )

        filename = (
            f"Quotation_{quotation_number}_"
            f"{safe_customer_name}.pdf"
        )

        return send_file(

            pdf_buffer,

            mimetype="application/pdf",

            as_attachment=True,

            download_name=filename
        )

    except Exception as error:

        app.logger.exception(
            "Quotation generation failed"
        )

        return jsonify({

            "success": False,

            "error": str(error)

        }), 500


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def safe_float(value):

    try:

        if value is None:
            return 0.0

        if isinstance(value, str):

            value = value.replace(
                ",",
                ""
            ).strip()

            if not value:
                return 0.0

        return float(value)

    except (
        ValueError,
        TypeError
    ):

        return 0.0


def format_money(value):

    try:

        return f"{float(value):,.2f}"

    except (
        ValueError,
        TypeError
    ):

        return "0.00"


def format_number(value):

    try:

        number = float(value)

        if number.is_integer():

            return str(int(number))

        return f"{number:,.2f}"

    except (
        ValueError,
        TypeError
    ):

        return "0"


def generate_quotation_number():

    now = datetime.now()

    return (
        f"KBS-{now.strftime('%Y%m%d')}-"
        f"{now.strftime('%H%M%S')}"
    )


def clean_filename(value):

    value = str(value)

    value = re.sub(
        r"[^A-Za-z0-9_-]+",
        "_",
        value
    )

    return value[:80]


def escape_html(value):

    value = str(value)

    return (
        value
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


# ============================================================
# ERROR HANDLERS
# ============================================================

@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "index.html"
    ), 404


@app.errorhandler(500)
def internal_server_error(error):

    return jsonify({

        "success": False,

        "error": "Internal server error. Please try again."

    }), 500


# ============================================================
# LOCAL DEVELOPMENT
# ============================================================

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(

        host="0.0.0.0",

        port=port,

        debug=False
    )
