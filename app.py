from flask import Flask, render_template, send_file, request
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
    PageBreak
)

from io import BytesIO
from datetime import datetime


# ============================================================
# APPLICATION
# ============================================================

app = Flask(__name__)

app.config["SECRET_KEY"] = "kenya-boreholes-services-2026"


# ============================================================
# PDF STYLES
# ============================================================

def pdf_styles():

    styles = getSampleStyleSheet()

    styles.add(
        ParagraphStyle(
            name="CompanyTitle",
            parent=styles["Heading1"],
            fontSize=18,
            leading=22,
            textColor=colors.HexColor("#1556a8"),
            alignment=TA_LEFT,
            spaceAfter=4
        )
    )

    styles.add(
        ParagraphStyle(
            name="DocumentTitle",
            parent=styles["Heading1"],
            fontSize=20,
            leading=24,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#1556a8"),
            spaceAfter=10
        )
    )

    styles.add(
        ParagraphStyle(
            name="SectionTitle",
            parent=styles["Heading2"],
            fontSize=13,
            leading=16,
            textColor=colors.HexColor("#1556a8"),
            spaceBefore=12,
            spaceAfter=7
        )
    )

    styles.add(
        ParagraphStyle(
            name="SmallText",
            parent=styles["Normal"],
            fontSize=8,
            leading=11
        )
    )

    return styles


# ============================================================
# COMMON PDF HEADER
# ============================================================

def pdf_header(story, title):

    styles = pdf_styles()

    header = Table(
        [
            [
                Paragraph(
                    "<b>KB</b>",
                    ParagraphStyle(
                        "Logo",
                        fontSize=18,
                        textColor=colors.white,
                        alignment=TA_CENTER
                    )
                ),

                Paragraph(
                    "<b>KENYA BOREHOLES SERVICES</b><br/>"
                    "<font size='9'>Professional Water Solutions Across Kenya</font>",
                    styles["CompanyTitle"]
                )
            ]
        ],
        colWidths=[25 * mm, 145 * mm]
    )

    header.setStyle(
        TableStyle(
            [
                (
                    "BACKGROUND",
                    (0, 0),
                    (0, 0),
                    colors.HexColor("#1556a8")
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                ),

                (
                    "LEFTPADDING",
                    (0, 0),
                    (-1, -1),
                    6
                ),

                (
                    "RIGHTPADDING",
                    (0, 0),
                    (-1, -1),
                    6
                ),

                (
                    "TOPPADDING",
                    (0, 0),
                    (-1, -1),
                    8
                ),

                (
                    "BOTTOMPADDING",
                    (0, 0),
                    (-1, -1),
                    8
                )
            ]
        )
    )

    story.append(header)
    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            title,
            styles["DocumentTitle"]
        )
    )

    story.append(
        Paragraph(
            f"Date: {datetime.now().strftime('%d/%m/%Y')}",
            styles["SmallText"]
        )
    )

    story.append(Spacer(1, 8))


# ============================================================
# GENERIC PDF
# ============================================================

def make_pdf(title, sections):

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=15 * mm,
        leftMargin=15 * mm,
        topMargin=15 * mm,
        bottomMargin=15 * mm
    )

    styles = pdf_styles()

    story = []

    pdf_header(story, title)

    for section_title, rows in sections:

        story.append(
            Paragraph(
                section_title,
                styles["SectionTitle"]
            )
        )

        table_data = []

        for row in rows:
            table_data.append(
                [
                    Paragraph(
                        str(cell),
                        styles["SmallText"]
                    )
                    for cell in row
                ]
            )

        table = Table(
            table_data,
            colWidths=[55 * mm, 115 * mm]
        )

        table.setStyle(
            TableStyle(
                [
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.5,
                        colors.HexColor("#b7c2cc")
                    ),

                    (
                        "BACKGROUND",
                        (0, 0),
                        (0, -1),
                        colors.HexColor("#edf4fa")
                    ),

                    (
                        "FONTNAME",
                        (0, 0),
                        (0, -1),
                        "Helvetica-Bold"
                    ),

                    (
                        "VALIGN",
                        (0, 0),
                        (-1, -1),
                        "TOP"
                    ),

                    (
                        "PADDING",
                        (0, 0),
                        (-1, -1),
                        7
                    )
                ]
            )
        )

        story.append(table)

        story.append(Spacer(1, 10))

    story.append(
        Spacer(1, 15)
    )

    story.append(
        Paragraph(
            "<b>KENYA BOREHOLES SERVICES</b><br/>"
            "Professional Water Solutions Across Kenya",
            styles["SmallText"]
        )
    )

    document.build(story)

    buffer.seek(0)

    return buffer


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():

    return render_template("index.html")


# ============================================================
# TEMPLATE: BLANK QUOTATION
# ============================================================

@app.route("/download-template/quotation")
def quotation_template():

    sections = [

        (
            "CUSTOMER INFORMATION",
            [
                ["Client Name", "________________________________________"],
                ["Phone Number", "________________________________________"],
                ["Email", "________________________________________"],
                ["Location", "________________________________________"]
            ]
        ),

        (
            "PROJECT INFORMATION",
            [
                ["Service / Project", "________________________________________"],
                ["Project Date", "________________________________________"],
                ["Quotation Reference", "________________________________________"],
                ["Validity", "________________________________________"]
            ]
        ),

        (
            "MATERIALS & REQUIREMENTS",
            [
                [
                    "Description",
                    "Quantity / Unit Price / Amount"
                ],
                [
                    "1. __________________________",
                    "____________________________"
                ],
                [
                    "2. __________________________",
                    "____________________________"
                ],
                [
                    "3. __________________________",
                    "____________________________"
                ],
                [
                    "4. __________________________",
                    "____________________________"
                ],
                [
                    "5. __________________________",
                    "____________________________"
                ]
            ]
        ),

        (
            "ADDITIONAL CHARGES",
            [
                ["Labour & Services", "KES __________________"],
                ["Transport & Logistics", "KES __________________"],
                ["TOTAL", "KES __________________"]
            ]
        ),

        (
            "TERMS & NOTES",
            [
                ["Notes", "______________________________________________"],
                ["", "______________________________________________"],
                ["", "______________________________________________"]
            ]
        )
    ]

    pdf = make_pdf(
        "BLANK QUOTATION FORM",
        sections
    )

    return send_file(
        pdf,
        as_attachment=True,
        download_name="Kenya_Boreholes_Blank_Quotation.pdf",
        mimetype="application/pdf"
    )


# ============================================================
# TEMPLATE: DELIVERY NOTE
# ============================================================

@app.route("/download-template/delivery-note")
def delivery_note_template():

    sections = [

        (
            "DELIVERY INFORMATION",
            [
                ["Delivery Note No.", "____________________________"],
                ["Date", "____________________________"],
                ["Customer", "____________________________"],
                ["Phone", "____________________________"],
                ["Delivery Location", "____________________________"]
            ]
        ),

        (
            "ITEMS DELIVERED",
            [
                ["Description", "Quantity"],
                ["____________________________", "____________"],
                ["____________________________", "____________"],
                ["____________________________", "____________"],
                ["____________________________", "____________"],
                ["____________________________", "____________"]
            ]
        ),

        (
            "DELIVERY DETAILS",
            [
                ["Vehicle Registration", "____________________________"],
                ["Driver Name", "____________________________"],
                ["Driver Phone", "____________________________"],
                ["Received By", "____________________________"],
                ["Receiver Phone", "____________________________"]
            ]
        ),

        (
            "CONDITION / REMARKS",
            [
                ["Remarks", "________________________________________"],
                ["", "________________________________________"],
                ["", "________________________________________"]
            ]
        ),

        (
            "SIGNATURES",
            [
                ["Delivered By", "____________________________"],
                ["Signature", "____________________________"],
                ["Received By", "____________________________"],
                ["Signature", "____________________________"]
            ]
        )
    ]

    pdf = make_pdf(
        "DELIVERY NOTE",
        sections
    )

    return send_file(
        pdf,
        as_attachment=True,
        download_name="Kenya_Boreholes_Delivery_Note.pdf",
        mimetype="application/pdf"
    )


# ============================================================
# TEMPLATE: WATER QUALITY REPORT
# ============================================================

@app.route("/download-template/water-quality-report")
def water_quality_report_template():

    sections = [

        (
            "SAMPLE INFORMATION",
            [
                ["Client Name", "____________________________"],
                ["Location", "____________________________"],
                ["Sample ID", "____________________________"],
                ["Sampling Date", "____________________________"],
                ["Testing Date", "____________________________"],
                ["Water Source", "____________________________"]
            ]
        ),

        (
            "PHYSICAL PARAMETERS",
            [
                ["Parameter", "Result / Unit"],
                ["Colour", "____________________________"],
                ["Odour", "____________________________"],
                ["Turbidity", "____________________________"],
                ["pH", "____________________________"],
                ["Electrical Conductivity", "____________________________"]
            ]
        ),

        (
            "CHEMICAL PARAMETERS",
            [
                ["Parameter", "Result / Unit"],
                ["Total Hardness", "____________________________"],
                ["Chloride", "____________________________"],
                ["Fluoride", "____________________________"],
                ["Nitrate", "____________________________"],
                ["Iron", "____________________________"]
            ]
        ),

        (
            "BACTERIOLOGICAL PARAMETERS",
            [
                ["Parameter", "Result / Unit"],
                ["Total Coliforms", "____________________________"],
                ["E. coli", "____________________________"]
            ]
        ),

        (
            "ASSESSMENT",
            [
                ["Overall Result", "____________________________"],
                ["Recommendations", "____________________________"],
                ["", "____________________________"]
            ]
        )
    ]

    pdf = make_pdf(
        "WATER QUALITY REPORT",
        sections
    )

    return send_file(
        pdf,
        as_attachment=True,
        download_name="Kenya_Boreholes_Water_Quality_Report.pdf",
        mimetype="application/pdf"
    )


# ============================================================
# TEMPLATE: BOREHOLE SURVEY
# ============================================================

@app.route("/download-template/borehole-survey")
def borehole_survey_template():

    sections = [

        (
            "CLIENT & SITE INFORMATION",
            [
                ["Client Name", "____________________________"],
                ["Phone", "____________________________"],
                ["Site Location", "____________________________"],
                ["County", "____________________________"],
                ["Sub-County", "____________________________"],
                ["GPS Coordinates", "____________________________"]
            ]
        ),

        (
            "SITE SURVEY",
            [
                ["Ground Elevation", "____________________________"],
                ["Terrain", "____________________________"],
                ["Existing Water Sources", "____________________________"],
                ["Nearby Boreholes", "____________________________"],
                ["Vegetation", "____________________________"],
                ["Accessibility", "____________________________"]
            ]
        ),

        (
            "GROUNDWATER OBSERVATIONS",
            [
                ["Expected Water Depth", "____________________________"],
                ["Expected Yield", "____________________________"],
                ["Water Table", "____________________________"],
                ["Geological Formation", "____________________________"],
                ["Recommended Drilling Depth", "____________________________"]
            ]
        ),

        (
            "SURVEY FINDINGS",
            [
                ["Recommended Site", "____________________________"],
                ["Survey Remarks", "____________________________"],
                ["", "____________________________"],
                ["", "____________________________"]
            ]
        ),

        (
            "AUTHORIZATION",
            [
                ["Surveyed By", "____________________________"],
                ["Designation", "____________________________"],
                ["Signature", "____________________________"],
                ["Date", "____________________________"]
            ]
        )
    ]

    pdf = make_pdf(
        "BOREHOLE SITE SURVEY SHEET",
        sections
    )

    return send_file(
        pdf,
        as_attachment=True,
        download_name="Kenya_Boreholes_Survey_Sheet.pdf",
        mimetype="application/pdf"
    )


# ============================================================
# WATER QUALITY ASSESSMENT PDF
# ============================================================

@app.route("/generate-water-quality", methods=["POST"])
def generate_water_quality():

    data = request.form

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=12 * mm,
        leftMargin=12 * mm,
        topMargin=12 * mm,
        bottomMargin=12 * mm
    )

    styles = pdf_styles()

    story = []

    pdf_header(
        story,
        "WATER QUALITY ASSESSMENT REPORT"
    )

    # --------------------------------------------------------
    # SAMPLE INFORMATION
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "SAMPLE INFORMATION",
            styles["SectionTitle"]
        )
    )

    sample_data = [
        ["Client Name", data.get("client_name", "")],
        ["Phone", data.get("phone", "")],
        ["Location", data.get("location", "")],
        ["Sample ID", data.get("sample_id", "")],
        ["Sampling Date", data.get("sampling_date", "")],
        ["Test Date", data.get("test_date", "")],
        ["Water Source", data.get("water_source", "")],
        ["Sample Point", data.get("sample_point", "")]
    ]

    sample_table = Table(
        sample_data,
        colWidths=[50 * mm, 120 * mm]
    )

    sample_table.setStyle(
        TableStyle(
            [
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.HexColor("#b7c2cc")
                ),

                (
                    "BACKGROUND",
                    (0, 0),
                    (0, -1),
                    colors.HexColor("#edf4fa")
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (0, -1),
                    "Helvetica-Bold"
                ),

                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    7
                )
            ]
        )
    )

    story.append(sample_table)


    # --------------------------------------------------------
    # QUALITY PARAMETER HELPER
    # --------------------------------------------------------

    def parameter_table(title, parameters):

        story.append(
            Paragraph(
                title,
                styles["SectionTitle"]
            )
        )

        rows = [
            [
                Paragraph("<b>Parameter</b>", styles["SmallText"]),
                Paragraph("<b>Result</b>", styles["SmallText"]),
                Paragraph("<b>Unit</b>", styles["SmallText"]),
                Paragraph("<b>Remarks</b>", styles["SmallText"])
            ]
        ]

        for parameter, result_key, unit, remarks_key in parameters:

            rows.append(
                [
                    parameter,
                    data.get(result_key, ""),
                    unit,
                    data.get(remarks_key, "")
                ]
            )

        table = Table(
            rows,
            colWidths=[
                55 * mm,
                35 * mm,
                30 * mm,
                50 * mm
            ]
        )

        table.setStyle(
            TableStyle(
                [
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.5,
                        colors.HexColor("#aebbc8")
                    ),

                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("#1556a8")
                    ),

                    (
                        "TEXTCOLOR",
                        (0, 0),
                        (-1, 0),
                        colors.white
                    ),

                    (
                        "FONTNAME",
                        (0, 0),
                        (-1, 0),
                        "Helvetica-Bold"
                    ),

                    (
                        "VALIGN",
                        (0, 0),
                        (-1, -1),
                        "MIDDLE"
                    ),

                    (
                        "PADDING",
                        (0, 0),
                        (-1, -1),
                        6
                    )
                ]
            )
        )

        story.append(table)

        story.append(
            Spacer(1, 8)
        )


    # --------------------------------------------------------
    # PHYSICAL
    # --------------------------------------------------------

    parameter_table(
        "PHYSICAL PARAMETERS",
        [
            (
                "Colour",
                "colour",
                "TCU",
                "colour_remarks"
            ),
            (
                "Odour",
                "odour",
                "-",
                "odour_remarks"
            ),
            (
                "Turbidity",
                "turbidity",
                "NTU",
                "turbidity_remarks"
            ),
            (
                "pH",
                "ph",
                "pH",
                "ph_remarks"
            ),
            (
                "Electrical Conductivity",
                "conductivity",
                "µS/cm",
                "conductivity_remarks"
            )
        ]
    )


    # --------------------------------------------------------
    # CHEMICAL
    # --------------------------------------------------------

    parameter_table(
        "CHEMICAL PARAMETERS",
        [
            (
                "Total Hardness",
                "hardness",
                "mg/L",
                "hardness_remarks"
            ),
            (
                "Chloride",
                "chloride",
                "mg/L",
                "chloride_remarks"
            ),
            (
                "Fluoride",
                "fluoride",
                "mg/L",
                "fluoride_remarks"
            ),
            (
                "Nitrate",
                "nitrate",
                "mg/L",
                "nitrate_remarks"
            ),
            (
                "Iron",
                "iron",
                "mg/L",
                "iron_remarks"
            )
        ]
    )


    # --------------------------------------------------------
    # BACTERIOLOGICAL
    # --------------------------------------------------------

    parameter_table(
        "BACTERIOLOGICAL PARAMETERS",
        [
            (
                "Total Coliforms",
                "total_coliforms",
                "CFU/100ml",
                "total_coliforms_remarks"
            ),
            (
                "E. coli",
                "ecoli",
                "CFU/100ml",
                "ecoli_remarks"
            )
        ]
    )


    # --------------------------------------------------------
    # ASSESSMENT
    # --------------------------------------------------------

    story.append(
        Paragraph(
            "ASSESSMENT & RECOMMENDATION",
            styles["SectionTitle"]
        )
    )

    assessment_data = [
        [
            "Overall Assessment",
            data.get("assessment", "")
        ],

        [
            "Recommendations",
            data.get("recommendations", "")
        ],

        [
            "Assessed By",
            data.get("assessed_by", "")
        ],

        [
            "Designation",
            data.get("designation", "")
        ]
    ]

    assessment_table = Table(
        assessment_data,
        colWidths=[50 * mm, 120 * mm]
    )

    assessment_table.setStyle(
        TableStyle(
            [
                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    0.5,
                    colors.HexColor("#b7c2cc")
                ),

                (
                    "BACKGROUND",
                    (0, 0),
                    (0, -1),
                    colors.HexColor("#edf4fa")
                ),

                (
                    "FONTNAME",
                    (0, 0),
                    (0, -1),
                    "Helvetica-Bold"
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "TOP"
                ),

                (
                    "PADDING",
                    (0, 0),
                    (-1, -1),
                    7
                )
            ]
        )
    )

    story.append(assessment_table)

    story.append(
        Spacer(1, 20)
    )

    story.append(
        Paragraph(
            "<b>KENYA BOREHOLES SERVICES</b><br/>"
            "Water Quality Assessment Department<br/>"
            "Professional Water Solutions Across Kenya",
            styles["SmallText"]
        )
    )

    document.build(story)

    buffer.seek(0)

    filename = (
        "Water_Quality_Assessment_"
        + datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".pdf"
    )

    return send_file(
        buffer,
        as_attachment=True,
        download_name=filename,
        mimetype="application/pdf"
    )


# ============================================================
# HEALTH CHECK
# ============================================================

@app.route("/health")
def health():

    return {
        "status": "ok",
        "application": "Kenya Boreholes Services"
    }


# ============================================================
# RUN LOCALLY
# ============================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
