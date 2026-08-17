/* =========================================================
   KENYA BOREHOLES SERVICES
   QUOTATION SYSTEM
========================================================= */


document.addEventListener(
    "DOMContentLoaded",
    function () {


        const quotationForm =
            document.getElementById(
                "quotationForm"
            );


        quotationForm.addEventListener(
            "submit",
            function (event) {

                event.preventDefault();

                generateQuotation();

            }
        );


        // Recalculate amounts when quantity or price changes

        document.addEventListener(
            "input",
            function (event) {

                if (
                    event.target.classList.contains(
                        "item-quantity"
                    )
                    ||
                    event.target.classList.contains(
                        "item-price"
                    )
                ) {

                    calculateItemAmount(
                        event.target.closest(
                            ".item-row"
                        )
                    );

                }

            }
        );


        calculateAllItems();

    }
);



/* =========================================================
   ADD ITEM
========================================================= */

function addItem() {

    const container =
        document.getElementById(
            "itemsContainer"
        );


    const row =
        document.createElement(
            "div"
        );


    row.className =
        "item-row";


    row.innerHTML = `

        <input
            type="text"
            class="item-description"
            placeholder="e.g. Drilling Consumables"
            required
        >

        <input
            type="number"
            class="item-quantity"
            value="1"
            min="0"
            step="0.01"
            required
        >

        <input
            type="number"
            class="item-price"
            value="0"
            min="0"
            step="0.01"
            required
        >

        <input
            type="text"
            class="item-amount"
            value="0.00"
            readonly
        >

        <button
            type="button"
            class="remove-item"
            onclick="removeItem(this)"
        >
            ×
        </button>

    `;


    container.appendChild(row);


    row
        .querySelector(".item-description")
        .focus();

}



/* =========================================================
   REMOVE ITEM
========================================================= */

function removeItem(button) {

    const container =
        document.getElementById(
            "itemsContainer"
        );


    const rows =
        container.querySelectorAll(
            ".item-row"
        );


    if (rows.length <= 1) {

        alert(
            "At least one quotation item is required."
        );

        return;

    }


    button
        .closest(".item-row")
        .remove();


    calculateAllItems();

}



/* =========================================================
   CALCULATE ITEM
========================================================= */

function calculateItemAmount(row) {

    if (!row) {
        return 0;
    }


    const quantity =
        Number(
            row.querySelector(
                ".item-quantity"
            ).value
        ) || 0;


    const price =
        Number(
            row.querySelector(
                ".item-price"
            ).value
        ) || 0;


    const amount =
        quantity * price;


    row.querySelector(
        ".item-amount"
    ).value =
        formatCurrency(amount);


    return amount;

}



/* =========================================================
   CALCULATE ALL ITEMS
========================================================= */

function calculateAllItems() {

    const rows =
        document.querySelectorAll(
            ".item-row"
        );


    let total = 0;


    rows.forEach(
        function (row) {

            total +=
                calculateItemAmount(
                    row
                );

        }
    );


    return total;

}



/* =========================================================
   GENERATE QUOTATION
========================================================= */

function generateQuotation() {


    const name =
        document.getElementById(
            "customerName"
        ).value.trim();


    const phone =
        document.getElementById(
            "phone"
        ).value.trim();


    const email =
        document.getElementById(
            "email"
        ).value.trim();


    const location =
        document.getElementById(
            "location"
        ).value.trim();


    const service =
        document.getElementById(
            "service"
        ).value;


    const capacity =
        document.getElementById(
            "capacity"
        ).value.trim();


    const projectDate =
        document.getElementById(
            "projectDate"
        ).value;


    const validity =
        document.getElementById(
            "validity"
        ).value.trim()
        ||
        "30 Days";


    const labour =
        Number(
            document.getElementById(
                "labour"
            ).value
        ) || 0;


    const transport =
        Number(
            document.getElementById(
                "transport"
            ).value
        ) || 0;


    const notes =
        document.getElementById(
            "notes"
        ).value.trim();



    /* =====================================================
       QUOTATION NUMBER
    ===================================================== */

    const now =
        new Date();


    const year =
        now.getFullYear();


    const month =
        String(
            now.getMonth() + 1
        ).padStart(2, "0");


    const day =
        String(
            now.getDate()
        ).padStart(2, "0");


    const random =
        Math.floor(
            1000 +
            Math.random() * 9000
        );


    const quotationNumber =
        "KBS/" +
        year +
        "/" +
        month +
        day +
        "/" +
        random;



    /* =====================================================
       DATE
    ===================================================== */

    const quotationDate =
        now.toLocaleDateString(
            "en-GB",
            {
                day: "2-digit",
                month: "long",
                year: "numeric"
            }
        );



    /* =====================================================
       CUSTOMER DETAILS
    ===================================================== */

    document.getElementById(
        "quotationNumber"
    ).textContent =
        quotationNumber;


    document.getElementById(
        "quotationDate"
    ).textContent =
        quotationDate;


    document.getElementById(
        "resultName"
    ).textContent =
        name;


    document.getElementById(
        "resultPhone"
    ).textContent =
        phone;


    document.getElementById(
        "resultEmail"
    ).textContent =
        email ||
        "Not provided";


    document.getElementById(
        "resultLocation"
    ).textContent =
        location;


    document.getElementById(
        "resultService"
    ).textContent =
        service;


    document.getElementById(
        "resultCapacity"
    ).textContent =
        capacity ||
        "Not specified";



    /* =====================================================
       ITEMS
    ===================================================== */

    const rows =
        document.querySelectorAll(
            ".item-row"
        );


    const quotationItems =
        document.getElementById(
            "quotationItems"
        );


    quotationItems.innerHTML = "";


    let materialsTotal = 0;


    let itemNumber = 1;


    rows.forEach(
        function (row) {

            const description =
                row.querySelector(
                    ".item-description"
                ).value.trim();


            const quantity =
                Number(
                    row.querySelector(
                        ".item-quantity"
                    ).value
                ) || 0;


            const price =
                Number(
                    row.querySelector(
                        ".item-price"
                    ).value
                ) || 0;


            const amount =
                quantity * price;


            materialsTotal +=
                amount;


            const tableRow =
                document.createElement(
                    "tr"
                );


            tableRow.innerHTML = `

                <td class="no-column">
                    ${itemNumber}
                </td>

                <td>
                    ${escapeHTML(description)}
                </td>

                <td class="quantity-column">
                    ${quantity}
                </td>

                <td class="price-column">
                    ${formatCurrency(price)}
                </td>

                <td class="amount-column">
                    ${formatCurrency(amount)}
                </td>

            `;


            quotationItems.appendChild(
                tableRow
            );


            itemNumber++;

        }
    );



    /* =====================================================
       TOTAL
    ===================================================== */

    const grandTotal =
        materialsTotal +
        labour +
        transport;


    document.getElementById(
        "resultLabour"
    ).textContent =
        formatCurrency(
            labour
        );


    document.getElementById(
        "resultTransport"
    ).textContent =
        formatCurrency(
            transport
        );


    document.getElementById(
        "grandTotal"
    ).textContent =
        "KES " +
        formatCurrency(
            grandTotal
        );



    /* =====================================================
       NOTES
    ===================================================== */

    const notesList =
        document.getElementById(
            "resultNotesList"
        );


    notesList.innerHTML = "";


    if (notes) {

        const customNotes =
            notes.split("\n");


        customNotes.forEach(
            function (note) {

                if (note.trim()) {

                    const li =
                        document.createElement(
                            "li"
                        );

                    li.textContent =
                        note.trim();

                    notesList.appendChild(
                        li
                    );

                }

            }
        );

    }



    /* =====================================================
       VALIDITY
    ===================================================== */

    document.getElementById(
        "validityText"
    ).textContent =
        "• This quotation is valid for " +
        validity +
        ".";



    /* =====================================================
       SHOW DOCUMENT
    ===================================================== */

    const result =
        document.getElementById(
            "quotationResult"
        );


    result.classList.remove(
        "hidden"
    );


    result.scrollIntoView(
        {
            behavior: "smooth",
            block: "start"
        }
    );

}



/* =========================================================
   CURRENCY
========================================================= */

function formatCurrency(amount) {

    return new Intl.NumberFormat(
        "en-KE",
        {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        }
    ).format(
        Number(amount) || 0
    );

}



/* =========================================================
   ESCAPE HTML
========================================================= */

function escapeHTML(value) {

    const div =
        document.createElement(
            "div"
        );


    div.textContent =
        value;


    return div.innerHTML;

}



/* =========================================================
   PRINT QUOTATION
========================================================= */

function printQuotation() {

    window.print();

}



/* =========================================================
   EDIT QUOTATION
========================================================= */

function editQuotation() {

    document.getElementById(
        "quotationForm"
    ).scrollIntoView(
        {
            behavior: "smooth"
        }
    );

}



/* =========================================================
   DOWNLOAD QUOTATION PDF
========================================================= */

function downloadQuotationPDF() {


    const quotation =
        document.getElementById(
            "quotationDocument"
        );


    const quotationNumber =
        document.getElementById(
            "quotationNumber"
        ).textContent;


    const customerName =
        document.getElementById(
            "resultName"
        ).textContent;


    const printWindow =
        window.open(
            "",
            "_blank"
        );


    if (!printWindow) {

        alert(
            "Please allow pop-ups in your browser to download the quotation."
        );

        return;

    }



    const documentHTML =
        quotation.innerHTML;



    printWindow.document.open();


    printWindow.document.write(`

        <!DOCTYPE html>

        <html>

        <head>

            <meta charset="UTF-8">

            <title>
                Quotation ${quotationNumber}
            </title>


            <style>

                @page {

                    size: A4;

                    margin: 10mm;

                }


                * {

                    box-sizing: border-box;

                }


                body {

                    margin: 0;

                    padding: 0;

                    font-family:
                        Arial,
                        Helvetica,
                        sans-serif;

                    color: #202020;

                    background: white;

                    font-size: 13px;

                }


                #quotationDocument {

                    width: 100%;

                    padding: 0;

                    background: white;

                }


                .document-top {

                    display: flex;

                    justify-content: space-between;

                    align-items: flex-start;

                    gap: 25px;

                }


                .document-company {

                    display: flex;

                    align-items: center;

                    gap: 12px;

                }


                .document-logo {

                    width: 55px;

                    height: 55px;

                    background: #1556a8;

                    color: white;

                    display: flex;

                    align-items: center;

                    justify-content: center;

                    font-weight: bold;

                    border-radius: 4px;

                }


                .document-company h1 {

                    margin: 0;

                    color: #1556a8;

                    font-size: 20px;

                }


                .document-company p {

                    margin: 2px 0;

                    color: #666;

                }


                .document-reference {

                    text-align: right;

                }


                .document-reference h2 {

                    margin: 0 0 7px;

                    font-size: 20px;

                }


                .document-reference p {

                    margin: 3px 0;

                }


                .document-line {

                    height: 2px;

                    background: #183e73;

                    margin: 15px 0 0;

                }


                .details-table {

                    margin-bottom: 20px;

                }


                .detail-row {

                    display: grid;

                    grid-template-columns:
                        175px
                        22px
                        1fr;

                    min-height: 34px;

                    align-items: center;

                    border-bottom:
                        1px solid #d7d7d7;

                }


                .detail-label {

                    font-weight: bold;

                }


                .detail-colon {

                    font-weight: bold;

                }


                .document-section-title {

                    color: #1556a8;

                    font-weight: bold;

                    font-size: 17px;

                    margin:
                        18px 0 8px;

                }


                .quotation-table {

                    width: 100%;

                    border-collapse: collapse;

                    font-size: 12px;

                }


                .quotation-table th {

                    background: #1556a8;

                    color: white;

                    border:
                        1px solid #8fa1b5;

                    padding: 8px 6px;

                    text-align: left;

                }


                .quotation-table td {

                    border:
                        1px solid #c8c8c8;

                    padding: 8px 6px;

                }


                .no-column {

                    width: 45px;

                    text-align: center;

                }


                .quantity-column {

                    width: 80px;

                    text-align: center;

                }


                .price-column {

                    width: 120px;

                    text-align: right;

                }


                .amount-column {

                    width: 125px;

                    text-align: right;

                }


                .money-cell {

                    text-align: right;

                }


                .special-row td {

                    background: #fafafa;

                }


                .total-row td {

                    background: #dce6f4;

                    color: #173c70;

                    font-weight: bold;

                    font-size: 14px;

                    padding: 10px 6px;

                }


                .total-row td:last-child {

                    text-align: right;

                }


                .terms-section {

                    margin-top: 20px;

                }


                .terms-section ul {

                    margin-top: 5px;

                    padding-left: 20px;

                }


                .terms-section li {

                    margin-bottom: 4px;

                }


                .standard-terms p {

                    margin: 3px 0;

                    font-size: 11px;

                }


                .document-footer {

                    margin-top: 25px;

                    padding-top: 12px;

                    border-top:
                        1px solid #c7c7c7;

                    display: flex;

                    justify-content: space-between;

                }


                .signature-box {

                    width: 170px;

                    text-align: center;

                }


                .signature-line {

                    border-bottom:
                        1px solid #555;

                    height: 28px;

                }


                @media print {

                    body {

                        -webkit-print-color-adjust:
                            exact;

                        print-color-adjust:
                            exact;

                    }

                }

            </style>

        </head>


        <body>

            <div id="quotationDocument">

                ${documentHTML}

            </div>

        </body>

        </html>

    `);


    printWindow.document.close();



    setTimeout(
        function () {

            printWindow.focus();

            printWindow.print();

        },
        700
    );

}
