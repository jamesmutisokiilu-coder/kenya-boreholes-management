from pathlib import Path
import zipfile
import webbrowser
import time


# ============================================================
# KENYA BOREHOLES SERVICES WEBSITE
# PROJECT GENERATOR
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

ZIP_PATH = BASE_DIR / "Kenya_Boreholes_Services_Website.zip"


# ============================================================
# WEBSITE FILES
# ============================================================

files_to_create = {

"index.html": r"""<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Kenya Boreholes Services</title>

    <link rel="stylesheet" href="styles.css">

</head>


<body>


<!-- =========================================================
     HEADER
========================================================= -->

<header class="header">

    <div class="logo">

        <div class="logo-icon">
            KB
        </div>

        <div>

            <h1>Kenya Boreholes Services</h1>

            <p>
                Reliable Water Solutions Across Kenya
            </p>

        </div>

    </div>


    <nav>

        <a href="#home">Home</a>
        <a href="#services">Services</a>
        <a href="#quotation">Quotation</a>
        <a href="#contact">Contact</a>

    </nav>

</header>



<!-- =========================================================
     HERO
========================================================= -->

<section id="home" class="hero">

    <div class="hero-content">

        <span class="hero-label">
            PROFESSIONAL WATER SOLUTIONS
        </span>

        <h2>
            Professional Borehole Services in Kenya
        </h2>

        <p>

            Complete borehole solutions including drilling,
            water testing, pump installation, maintenance,
            site surveys and water delivery.

        </p>


        <div class="hero-buttons">

            <a
                href="#quotation"
                class="btn primary"
            >
                Request Quotation
            </a>


            <a
                href="#services"
                class="btn secondary"
            >
                View Services
            </a>

        </div>

    </div>

</section>



<!-- =========================================================
     SERVICES
========================================================= -->

<section id="services" class="section">

    <div class="section-title">

        <span>WHAT WE OFFER</span>

        <h2>
            Our Borehole Services
        </h2>

        <p>

            Professional and affordable water solutions
            for homes, farms, institutions and businesses.

        </p>

    </div>


    <div class="services-grid">


        <div class="service-card">

            <div class="service-icon">
                💧
            </div>

            <h3>
                Borehole Drilling
            </h3>

            <p>

                Professional borehole drilling services
                using modern equipment and experienced
                technicians.

            </p>

        </div>



        <div class="service-card">

            <div class="service-icon">
                🔬
            </div>

            <h3>
                Water Testing
            </h3>

            <p>

                Laboratory water quality testing to determine
                whether your borehole water is suitable
                for use.

            </p>

        </div>



        <div class="service-card">

            <div class="service-icon">
                ⚙️
            </div>

            <h3>
                Pump Installation
            </h3>

            <p>

                Installation of reliable submersible,
                solar and other pumping systems.

            </p>

        </div>



        <div class="service-card">

            <div class="service-icon">
                🔧
            </div>

            <h3>
                Maintenance
            </h3>

            <p>

                Borehole inspection, pump repair,
                servicing and maintenance.

            </p>

        </div>



        <div class="service-card">

            <div class="service-icon">
                🚚
            </div>

            <h3>
                Water Delivery
            </h3>

            <p>

                Water transportation and delivery services
                for homes, construction sites and businesses.

            </p>

        </div>



        <div class="service-card">

            <div class="service-icon">
                📍
            </div>

            <h3>
                Site Survey
            </h3>

            <p>

                Professional site assessment and groundwater
                survey before drilling.

            </p>

        </div>


    </div>

</section>



<!-- =========================================================
     QUOTATION FORM
========================================================= -->

<section
    id="quotation"
    class="quotation-section"
>


    <div class="section-title">

        <span>GET STARTED</span>

        <h2>
            Prepare a Professional Quotation
        </h2>

        <p>

            Enter your customer and project information
            below. You can add multiple materials,
            services and charges.

        </p>

    </div>



    <div class="quotation-container">


        <form id="quotationForm">


            <!-- CUSTOMER INFORMATION -->

            <div class="form-heading">

                <span>
                    01
                </span>

                <div>

                    <h3>
                        Customer Information
                    </h3>

                    <p>
                        Enter the customer's details.
                    </p>

                </div>

            </div>



            <div class="form-grid">


                <div class="form-group">

                    <label>
                        Client Name *
                    </label>

                    <input
                        type="text"
                        id="customerName"
                        placeholder="e.g. Karen Tank Services"
                        required
                    >

                </div>



                <div class="form-group">

                    <label>
                        Phone Number *
                    </label>

                    <input
                        type="tel"
                        id="phone"
                        placeholder="e.g. 0712345678"
                        required
                    >

                </div>



                <div class="form-group">

                    <label>
                        Email
                    </label>

                    <input
                        type="email"
                        id="email"
                        placeholder="customer@example.com"
                    >

                </div>



                <div class="form-group">

                    <label>
                        Location *
                    </label>

                    <input
                        type="text"
                        id="location"
                        placeholder="e.g. Karen, Nairobi"
                        required
                    >

                </div>



            </div>



            <!-- PROJECT INFORMATION -->

            <div class="form-heading second-heading">

                <span>
                    02
                </span>

                <div>

                    <h3>
                        Project Information
                    </h3>

                    <p>
                        Details that will appear on the quotation.
                    </p>

                </div>

            </div>



            <div class="form-grid">


                <div class="form-group">

                    <label>
                        Service / Project *
                    </label>

                    <select
                        id="service"
                        required
                    >

                        <option value="">
                            Select Service
                        </option>

                        <option>
                            Borehole Drilling
                        </option>

                        <option>
                            Borehole Maintenance
                        </option>

                        <option>
                            Water Testing
                        </option>

                        <option>
                            Pump Installation
                        </option>

                        <option>
                            Water Delivery
                        </option>

                        <option>
                            Site Survey
                        </option>

                        <option>
                            Borehole Equipping
                        </option>

                        <option>
                            Tank Cleaning & Servicing
                        </option>

                        <option>
                            Other
                        </option>

                    </select>

                </div>



                <div class="form-group">

                    <label>
                        Project / Tank Capacity
                    </label>

                    <input
                        type="text"
                        id="capacity"
                        placeholder="e.g. 100,000 Litres"
                    >

                </div>



                <div class="form-group">

                    <label>
                        Project Date
                    </label>

                    <input
                        type="date"
                        id="projectDate"
                    >

                </div>



                <div class="form-group">

                    <label>
                        Validity
                    </label>

                    <input
                        type="text"
                        id="validity"
                        value="30 Days"
                    >

                </div>


            </div>



            <!-- ITEMS -->

            <div class="form-heading second-heading">

                <span>
                    03
                </span>

                <div>

                    <h3>
                        Materials & Requirements
                    </h3>

                    <p>
                        Add all materials, labour and services.
                    </p>

                </div>

            </div>



            <div class="items-form">


                <div class="items-header">

                    <div>
                        Description
                    </div>

                    <div>
                        Quantity
                    </div>

                    <div>
                        Unit Price (KES)
                    </div>

                    <div>
                        Amount (KES)
                    </div>

                    <div>
                    </div>

                </div>


                <div id="itemsContainer">


                    <div class="item-row">

                        <input
                            type="text"
                            class="item-description"
                            placeholder="e.g. Submersible Pump"
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

                    </div>


                </div>



                <button
                    type="button"
                    class="add-item-btn"
                    onclick="addItem()"
                >

                    + Add Another Item

                </button>


            </div>



            <!-- EXTRA CHARGES -->

            <div class="form-grid extra-charges">


                <div class="form-group">

                    <label>
                        Labour & Service (KES)
                    </label>

                    <input
                        type="number"
                        id="labour"
                        value="0"
                        min="0"
                        step="0.01"
                    >

                </div>



                <div class="form-group">

                    <label>
                        Transport & Logistics (KES)
                    </label>

                    <input
                        type="number"
                        id="transport"
                        value="0"
                        min="0"
                        step="0.01"
                    >

                </div>


            </div>



            <!-- NOTES -->

            <div class="form-group">

                <label>
                    Terms & Notes
                </label>

                <textarea
                    id="notes"
                    rows="6"
                    placeholder="Enter quotation terms, conditions, site requirements, payment terms or other notes..."
                ></textarea>

            </div>



            <button
                type="submit"
                class="btn primary full-btn"
            >

                Generate Professional Quotation

            </button>


        </form>



        <!-- =================================================
             QUOTATION RESULT
        ================================================= -->

        <div
            id="quotationResult"
            class="quotation-result hidden"
        >


            <!-- DOCUMENT -->

            <div id="quotationDocument">


                <!-- DOCUMENT HEADER -->

                <div class="document-top">


                    <div class="document-company">


                        <div class="document-logo">
                            KB
                        </div>


                        <div>

                            <h1>
                                KENYA BOREHOLES SERVICES
                            </h1>

                            <p>
                                Professional Water Solutions
                            </p>

                        </div>


                    </div>



                    <div class="document-reference">

                        <h2>
                            <span id="documentTitle">
                                QUOTATION
                            </span>
                        </h2>

                        <p>
                            <strong>
                                Quotation Ref:
                            </strong>

                            <span id="quotationNumber">
                            </span>
                        </p>

                        <p>
                            <strong>
                                Date:
                            </strong>

                            <span id="quotationDate">
                            </span>
                        </p>

                    </div>


                </div>



                <div class="document-line">
                </div>



                <!-- CUSTOMER / PROJECT DETAILS -->

                <div class="details-table">


                    <div class="detail-row">

                        <div class="detail-label">
                            Client
                        </div>

                        <div class="detail-colon">
                            :
                        </div>

                        <div id="resultName">
                        </div>

                    </div>



                    <div class="detail-row">

                        <div class="detail-label">
                            Location
                        </div>

                        <div class="detail-colon">
                            :
                        </div>

                        <div id="resultLocation">
                        </div>

                    </div>



                    <div class="detail-row">

                        <div class="detail-label">
                            Contact
                        </div>

                        <div class="detail-colon">
                            :
                        </div>

                        <div id="resultPhone">
                        </div>

                    </div>



                    <div class="detail-row">

                        <div class="detail-label">
                            Email
                        </div>

                        <div class="detail-colon">
                            :
                        </div>

                        <div id="resultEmail">
                        </div>

                    </div>



                    <div class="detail-row">

                        <div class="detail-label">
                            Project / Service
                        </div>

                        <div class="detail-colon">
                            :
                        </div>

                        <div id="resultService">
                        </div>

                    </div>



                    <div
                        class="detail-row"
                        id="capacityRow"
                    >

                        <div class="detail-label">
                            Capacity
                        </div>

                        <div class="detail-colon">
                            :
                        </div>

                        <div id="resultCapacity">
                        </div>

                    </div>


                </div>



                <!-- SECTION TITLE -->

                <div class="document-section-title">

                    MATERIALS & REQUIREMENTS

                </div>



                <!-- QUOTATION TABLE -->

                <table
                    class="quotation-table"
                    id="quotationItemsTable"
                >

                    <thead>

                        <tr>

                            <th class="no-column">
                                No.
                            </th>

                            <th>
                                Description
                            </th>

                            <th class="quantity-column">
                                Quantity
                            </th>

                            <th class="price-column">
                                Unit Price (KES)
                            </th>

                            <th class="amount-column">
                                Amount (KES)
                            </th>

                        </tr>

                    </thead>


                    <tbody id="quotationItems">

                    </tbody>


                    <tbody>


                        <tr class="special-row">

                            <td colspan="4">
                                Labour & Tank/Borehole Servicing
                            </td>

                            <td
                                id="resultLabour"
                                class="money-cell"
                            >
                                0.00
                            </td>

                        </tr>



                        <tr class="special-row">

                            <td colspan="4">
                                Transport & Logistics
                            </td>

                            <td
                                id="resultTransport"
                                class="money-cell"
                            >
                                0.00
                            </td>

                        </tr>


                    </tbody>



                    <tfoot>

                        <tr class="total-row">

                            <td colspan="4">
                                TOTAL QUOTATION
                            </td>

                            <td id="grandTotal">
                                KES 0.00
                            </td>

                        </tr>

                    </tfoot>


                </table>



                <!-- TERMS -->

                <div class="terms-section">


                    <div class="document-section-title">

                        TERMS & NOTES

                    </div>


                    <ul id="resultNotesList">

                    </ul>


                    <div class="standard-terms">

                        <p>
                            • Quotation is based on the listed
                            materials and stated project scope.
                        </p>

                        <p>
                            • Any additional repairs or materials
                            required after inspection will be
                            communicated and quoted separately.
                        </p>

                        <p>
                            • Prices are subject to confirmation
                            before commencement of works.
                        </p>

                        <p>
                            • Site assessment may be required
                            before final confirmation.
                        </p>

                        <p id="validityText">
                            • This quotation is valid for 30 Days.
                        </p>

                    </div>


                </div>



                <!-- FOOTER -->

                <div class="document-footer">


                    <div>

                        <strong>
                            KENYA BOREHOLES SERVICES
                        </strong>

                        <p>
                            Professional Water Solutions Across Kenya
                        </p>

                    </div>


                    <div class="signature-box">

                        <p>
                            Authorized By
                        </p>

                        <div class="signature-line">
                        </div>

                    </div>


                </div>


            </div>



            <!-- ACTIONS -->

            <div class="quotation-actions">


                <button
                    class="btn primary"
                    onclick="downloadQuotationPDF()"
                >
                    Download Quotation PDF
                </button>



                <button
                    class="btn secondary"
                    onclick="printQuotation()"
                >
                    Print Quotation
                </button>



                <button
                    class="btn outline-btn"
                    onclick="editQuotation()"
                >
                    Edit Quotation
                </button>


            </div>


        </div>


    </div>

</section>



<!-- =========================================================
     CONTACT
========================================================= -->

<section
    id="contact"
    class="contact-section"
>

    <div class="section-title">

        <span>
            CONTACT US
        </span>

        <h2>
            Let's Discuss Your Water Project
        </h2>

    </div>



    <div class="contact-grid">


        <div class="contact-card">

            <h3>
                Phone
            </h3>

            <p>
                +254 700 000 000
            </p>

        </div>



        <div class="contact-card">

            <h3>
                Email
            </h3>

            <p>
                info@kenyaboreholes.co.ke
            </p>

        </div>



        <div class="contact-card">

            <h3>
                Location
            </h3>

            <p>
                Kenya
            </p>

        </div>


    </div>

</section>



<footer>

    <p>
        © 2026 Kenya Boreholes Services.
        All Rights Reserved.
    </p>

</footer>



<script src="app.js"></script>

</body>

</html>
""",



"styles.css": r"""* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}


html {
    scroll-behavior: smooth;
}


body {
    font-family: Arial, Helvetica, sans-serif;
    background: #f4f7fa;
    color: #17212b;
    line-height: 1.6;
}


/* =========================================================
   HEADER
========================================================= */

.header {
    background: #ffffff;
    min-height: 80px;
    padding: 15px 6%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 30px;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
}


.logo {
    display: flex;
    align-items: center;
    gap: 12px;
}


.logo-icon {
    width: 48px;
    height: 48px;
    border-radius: 10px;
    background: #1556a8;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
}


.logo h1 {
    font-size: 20px;
}


.logo p {
    color: #687582;
    font-size: 12px;
}


nav {
    display: flex;
    gap: 25px;
}


nav a {
    text-decoration: none;
    color: #17212b;
    font-weight: 600;
}


nav a:hover {
    color: #1556a8;
}



/* =========================================================
   HERO
========================================================= */

.hero {
    min-height: 580px;

    background:
        linear-gradient(
            rgba(5, 41, 70, 0.84),
            rgba(5, 41, 70, 0.84)
        ),
        linear-gradient(
            135deg,
            #1687e8,
            #0d527e
        );

    display: flex;
    align-items: center;
    justify-content: center;

    text-align: center;

    padding: 80px 20px;

    color: white;
}


.hero-content {
    max-width: 850px;
}


.hero-label {
    font-size: 13px;
    letter-spacing: 3px;
    font-weight: bold;
}


.hero h2 {
    font-size: 52px;
    line-height: 1.15;
    margin: 18px 0 20px;
}


.hero p {
    font-size: 20px;
    max-width: 700px;
    margin: auto;
    color: #eaf6ff;
}


.hero-buttons {
    margin-top: 35px;

    display: flex;
    justify-content: center;

    gap: 15px;

    flex-wrap: wrap;
}



/* =========================================================
   BUTTONS
========================================================= */

.btn {
    border: none;

    padding: 14px 25px;

    border-radius: 8px;

    font-weight: bold;

    cursor: pointer;

    text-decoration: none;

    display: inline-block;

    transition: 0.2s;
}


.btn:hover {
    transform: translateY(-2px);
}


.primary {
    background: #1687e8;
    color: white;
}


.secondary {
    background: white;
    color: #1687e8;
}


.outline-btn {
    background: white;
    color: #1556a8;
    border: 1px solid #1556a8;
}



/* =========================================================
   SECTIONS
========================================================= */

.section,
.quotation-section,
.contact-section {
    padding: 80px 7%;
}


.section-title {
    text-align: center;

    max-width: 750px;

    margin: 0 auto 45px;
}


.section-title span {
    color: #1556a8;

    font-size: 13px;

    font-weight: bold;

    letter-spacing: 2px;
}


.section-title h2 {
    font-size: 38px;

    margin: 8px 0;
}


.section-title p {
    color: #687582;
}



/* =========================================================
   SERVICES
========================================================= */

.services-grid {
    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 25px;
}


.service-card {
    background: white;

    padding: 30px;

    border-radius: 14px;

    box-shadow:
        0 5px 20px rgba(0,0,0,0.06);

    border:
        1px solid #e6edf3;
}


.service-icon {
    font-size: 35px;

    margin-bottom: 15px;
}


.service-card h3 {
    margin-bottom: 10px;
}


.service-card p {
    color: #687582;
}



/* =========================================================
   QUOTATION FORM
========================================================= */

.quotation-section {
    background: #edf4fa;
}


.quotation-container {
    max-width: 1100px;
    margin: auto;
}


#quotationForm {
    background: white;

    padding: 38px;

    border-radius: 15px;

    box-shadow:
        0 5px 25px rgba(0,0,0,0.07);
}


.form-heading {
    display: flex;

    align-items: center;

    gap: 15px;

    border-bottom:
        1px solid #e2e8ee;

    padding-bottom: 18px;

    margin-bottom: 25px;
}


.form-heading > span {
    width: 42px;
    height: 42px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background: #1556a8;

    color: white;

    font-weight: bold;
}


.form-heading h3 {
    margin-bottom: 2px;
}


.form-heading p {
    color: #7a8791;
    font-size: 13px;
}


.second-heading {
    margin-top: 35px;
}


.form-grid {
    display: grid;

    grid-template-columns:
        repeat(2, 1fr);

    gap: 20px;
}


.form-group {
    margin-bottom: 20px;
}


.form-group label {
    display: block;

    margin-bottom: 7px;

    font-weight: bold;

    font-size: 14px;
}


input,
select,
textarea {
    width: 100%;

    padding: 13px;

    border:
        1px solid #ccd7df;

    border-radius: 7px;

    font-size: 15px;

    outline: none;

    background: white;
}


input:focus,
select:focus,
textarea:focus {
    border-color: #1687e8;

    box-shadow:
        0 0 0 3px rgba(22,135,232,0.10);
}


textarea {
    resize: vertical;
}


.full-btn {
    width: 100%;

    font-size: 16px;

    margin-top: 10px;
}



/* =========================================================
   ITEMS
========================================================= */

.items-form {
    border:
        1px solid #dce5eb;

    border-radius: 10px;

    overflow: hidden;

    margin-bottom: 25px;
}


.items-header,
.item-row {
    display: grid;

    grid-template-columns:
        minmax(200px, 2fr)
        120px
        170px
        170px
        50px;

    gap: 0;

    align-items: center;
}


.items-header {
    background: #1556a8;

    color: white;

    font-weight: bold;

    padding: 13px;
}


.item-row {
    padding: 10px;

    border-top:
        1px solid #e1e7ec;
}


.item-row input {
    border-radius: 4px;

    margin: 0 5px;
}


.item-amount {
    background: #f3f6f8;

    font-weight: bold;
}


.remove-item {
    width: 34px;
    height: 34px;

    border: none;

    border-radius: 50%;

    background: #ffe8e8;

    color: #d32929;

    font-size: 22px;

    cursor: pointer;
}


.add-item-btn {
    margin: 15px;

    padding: 10px 18px;

    border:
        1px dashed #1556a8;

    color: #1556a8;

    background: #f5f9fd;

    border-radius: 6px;

    cursor: pointer;

    font-weight: bold;
}


.extra-charges {
    margin-top: 20px;
}



/* =========================================================
   QUOTATION RESULT
========================================================= */

.quotation-result {
    margin-top: 35px;

    background: #dfe7ee;

    padding: 25px;

    border-radius: 10px;
}


.hidden {
    display: none;
}



/* =========================================================
   ACTUAL QUOTATION DOCUMENT
========================================================= */

#quotationDocument {
    background: white;

    width: 100%;

    max-width: 1000px;

    margin: auto;

    padding: 38px;

    box-shadow:
        0 5px 25px rgba(0,0,0,0.12);

    color: #202020;
}


.document-top {
    display: flex;

    justify-content: space-between;

    align-items: flex-start;

    gap: 30px;
}


.document-company {
    display: flex;

    align-items: center;

    gap: 14px;
}


.document-logo {
    width: 58px;
    height: 58px;

    background: #1556a8;

    color: white;

    display: flex;

    align-items: center;
    justify-content: center;

    font-size: 20px;

    font-weight: bold;

    border-radius: 5px;
}


.document-company h1 {
    font-size: 22px;

    color: #1556a8;

    letter-spacing: 0.5px;
}


.document-company p {
    color: #666;

    font-size: 13px;
}


.document-reference {
    text-align: right;

    min-width: 240px;
}


.document-reference h2 {
    font-size: 22px;

    color: #111;

    margin-bottom: 10px;
}


.document-reference p {
    font-size: 14px;

    margin: 3px 0;
}


.document-line {
    height: 2px;

    background: #183e73;

    margin:
        18px 0 0;
}



/* =========================================================
   CUSTOMER DETAILS
========================================================= */

.details-table {
    margin-top: 5px;

    margin-bottom: 28px;
}


.detail-row {
    display: grid;

    grid-template-columns:
        180px
        25px
        1fr;

    min-height: 40px;

    align-items: center;

    border-bottom:
        1px solid #d7d7d7;

    font-size: 15px;
}


.detail-label {
    font-weight: bold;
}


.detail-colon {
    font-weight: bold;
}



/* =========================================================
   SECTION TITLE
========================================================= */

.document-section-title {
    color: #1556a8;

    font-size: 19px;

    font-weight: bold;

    margin:
        20px 0 10px;
}



/* =========================================================
   QUOTATION TABLE
========================================================= */

.quotation-table {
    width: 100%;

    border-collapse: collapse;

    margin-top: 10px;

    font-size: 14px;
}


.quotation-table th {
    background: #1556a8;

    color: white;

    border:
        1px solid #9baec3;

    padding: 11px 8px;

    text-align: left;
}


.quotation-table td {
    border:
        1px solid #c7c7c7;

    padding: 10px 8px;

    vertical-align: middle;
}


.quotation-table tbody tr:nth-child(even) {
    background: #fafafa;
}


.no-column {
    width: 55px;

    text-align: center !important;
}


.quantity-column {
    width: 105px;

    text-align: center !important;
}


.price-column {
    width: 155px;

    text-align: right !important;
}


.amount-column {
    width: 160px;

    text-align: right !important;
}


.money-cell {
    text-align: right;

    font-weight: 600;
}


.special-row td {
    background: #fafafa;
}


.special-row td:first-child {
    font-weight: 500;
}


.total-row td {
    background: #dce6f4;

    color: #173c70;

    font-weight: bold;

    font-size: 17px;

    padding: 13px 8px;
}


.total-row td:last-child {
    text-align: right;
}



/* =========================================================
   TERMS
========================================================= */

.terms-section {
    margin-top: 25px;
}


.terms-section ul {
    margin:
        5px 0 12px 22px;
}


.terms-section li {
    margin-bottom: 5px;
}


.standard-terms p {
    font-size: 13px;

    margin: 4px 0;
}



/* =========================================================
   DOCUMENT FOOTER
========================================================= */

.document-footer {
    margin-top: 35px;

    padding-top: 18px;

    border-top:
        1px solid #c7c7c7;

    display: flex;

    justify-content: space-between;

    gap: 30px;

    font-size: 13px;

    color: #555;
}


.signature-box {
    min-width: 190px;

    text-align: center;
}


.signature-line {
    height: 35px;

    border-bottom:
        1px solid #555;

    margin-top: 5px;
}



/* =========================================================
   ACTIONS
========================================================= */

.quotation-actions {
    display: flex;

    justify-content: center;

    gap: 15px;

    margin-top: 25px;

    flex-wrap: wrap;
}



/* =========================================================
   CONTACT
========================================================= */

.contact-section {
    background: white;
}


.contact-grid {
    max-width: 1000px;

    margin: auto;

    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 25px;
}


.contact-card {
    padding: 30px;

    text-align: center;

    background: #f5f8fb;

    border-radius: 12px;
}


.contact-card h3 {
    color: #1556a8;

    margin-bottom: 10px;
}



/* =========================================================
   FOOTER
========================================================= */

footer {
    background: #062a45;

    color: white;

    padding: 30px;

    text-align: center;
}



/* =========================================================
   PRINT
========================================================= */

@media print {

    @page {
        size: A4;
        margin: 10mm;
    }


    body {
        background: white !important;
    }


    body * {
        visibility: hidden;
    }


    #quotationDocument,
    #quotationDocument * {
        visibility: visible;
    }


    #quotationDocument {
        position: absolute;

        left: 0;
        top: 0;

        width: 100%;

        max-width: none;

        padding: 0;

        margin: 0;

        box-shadow: none;
    }


    .quotation-actions {
        display: none !important;
    }


    .quotation-result {
        background: white;

        padding: 0;

        margin: 0;
    }


    .document-top {
        break-inside: avoid;
    }


    .quotation-table {
        break-inside: auto;
    }


    .quotation-table tr {
        break-inside: avoid;
        page-break-inside: avoid;
    }


    .terms-section {
        break-inside: avoid;
    }


    .document-footer {
        break-inside: avoid;
    }

}



/* =========================================================
   RESPONSIVE
========================================================= */

@media (max-width: 900px) {

    .header {
        flex-direction: column;
    }


    nav {
        flex-wrap: wrap;

        justify-content: center;
    }


    .hero h2 {
        font-size: 38px;
    }


    .services-grid,
    .contact-grid {
        grid-template-columns: 1fr;
    }


    .form-grid {
        grid-template-columns: 1fr;
    }


    .items-form {
        overflow-x: auto;
    }


    .items-header,
    .item-row {
        min-width: 850px;
    }


    .document-top {
        flex-direction: column;
    }


    .document-reference {
        text-align: left;
    }

}


@media (max-width: 600px) {

    .section,
    .quotation-section,
    .contact-section {
        padding: 55px 5%;
    }


    .hero {
        min-height: 500px;
    }


    .hero h2 {
        font-size: 32px;
    }


    .hero p {
        font-size: 17px;
    }


    #quotationForm {
        padding: 20px;
    }


    #quotationDocument {
        padding: 20px;
    }


    .document-company h1 {
        font-size: 17px;
    }


    .document-reference {
        min-width: 0;
    }


    .detail-row {
        grid-template-columns:
            120px
            20px
            1fr;

        font-size: 12px;
    }


    .quotation-table {
        font-size: 10px;
    }


    .quotation-table th,
    .quotation-table td {
        padding: 7px 4px;
    }


    .document-footer {
        flex-direction: column;
    }

}
""",



"app.js": r"""/* =========================================================
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
""",



"README.txt": r"""============================================================
KENYA BOREHOLES SERVICES WEBSITE
============================================================

Professional borehole services website with a quotation
generation system.

FILES
------------------------------------------------------------

index.html
Main website.

styles.css
Website styling and professional quotation styling.

app.js
Quotation generation, calculations, printing and PDF
printing functionality.

README.txt
Project documentation.

FEATURES
------------------------------------------------------------

1. Professional home page
2. Borehole drilling services
3. Water testing
4. Pump installation
5. Borehole maintenance
6. Water delivery
7. Site survey
8. Professional quotation form
9. Multiple quotation items
10. Automatic item calculations
11. Labour & Service charges
12. Transport & Logistics charges
13. Automatic quotation reference
14. Automatic quotation date
15. Customer details
16. Project details
17. Materials & Requirements table
18. Total quotation
19. Terms & Notes
20. Print quotation
21. Save quotation as PDF using browser Print > Save as PDF
22. Responsive design
23. Automatically opens in browser when app.py is run
24. ZIP project generation

QUOTATION DESIGN
------------------------------------------------------------

The quotation has been designed using the supplied quotation
example as the visual reference.

It contains:

KENYA BOREHOLES SERVICES

QUOTATION

Quotation Ref
Date

Client
Location
Contact
Email
Project / Service
Capacity

MATERIALS & REQUIREMENTS

No.
Description
Quantity
Unit Price (KES)
Amount (KES)

Labour & Borehole Servicing
Transport & Logistics

TOTAL QUOTATION

TERMS & NOTES

Authorized By

PDF
------------------------------------------------------------

When the user clicks:

Download Quotation PDF

a separate quotation document opens in the browser print
window.

Choose:

Save as PDF

The resulting PDF contains the quotation only, rather than
the whole website.

OPENING THE WEBSITE
------------------------------------------------------------

Run:

python app.py

The program will:

1. Create index.html
2. Create styles.css
3. Create app.js
4. Create README.txt
5. Create Kenya_Boreholes_Services_Website.zip
6. Open index.html automatically in the default browser

You can also open index.html directly.

VISUAL STUDIO CODE
------------------------------------------------------------

Open the project folder in Visual Studio Code.

Install the Live Server extension.

Right-click:

index.html

Then select:

Open with Live Server

The website will open in your browser.

IMPORTANT
------------------------------------------------------------

The Python generator does not need Flask.

It generates a static website.

The quotation calculations are handled by JavaScript.

============================================================
"""
}


# ============================================================
# CREATE PROJECT DIRECTORY
# ============================================================

BASE_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# CREATE WEBSITE FILES
# ============================================================

print()
print("Creating Kenya Boreholes Services Website...")
print()


for filename, content in files_to_create.items():

    file_path = BASE_DIR / filename

    file_path.write_text(
        content,
        encoding="utf-8"
    )

    print(
        f"Created: {file_path}"
    )


# ============================================================
# CREATE ZIP FILE
# ============================================================

if ZIP_PATH.exists():

    ZIP_PATH.unlink()


with zipfile.ZipFile(
    ZIP_PATH,
    "w",
    zipfile.ZIP_DEFLATED
) as archive:

    for filename in files_to_create.keys():

        file_path = BASE_DIR / filename

        archive.write(
            file_path,
            arcname=filename
        )

        print(
            f"Added to ZIP: {filename}"
        )


# ============================================================
# SUCCESS MESSAGE
# ============================================================

print()

print("=" * 65)
print(
    "KENYA BOREHOLES SERVICES WEBSITE"
)
print(
    "PROJECT CREATED SUCCESSFULLY"
)
print("=" * 65)

print(
    f"Project location: {BASE_DIR}"
)

print(
    f"ZIP file created: {ZIP_PATH}"
)

print()

print(
    "Files included:"
)


for filename in files_to_create.keys():

    # ASCII only.
    # Prevents Windows CP1252 UnicodeEncodeError.

    print(
        f"  [OK] {filename}"
    )


print()

print("=" * 65)
print(
    "OPENING WEBSITE IN YOUR DEFAULT BROWSER..."
)
print("=" * 65)


# ============================================================
# OPEN WEBSITE AUTOMATICALLY
# ============================================================

index_file = BASE_DIR / "index.html"


if index_file.exists():

    browser_url = (
        index_file
        .resolve()
        .as_uri()
    )

    print()

    print(
        f"Opening: {browser_url}"
    )

    print()

    time.sleep(1)

    webbrowser.open(
        browser_url
    )

else:

    print()

    print(
        "ERROR: index.html was not created."
    )

    print()


print("=" * 65)

print(
    "DONE"
)

print("=" * 65)