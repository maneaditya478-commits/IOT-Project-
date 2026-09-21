"""
Generate Microsoft Word (.docx) Document for Patent Draft Application
Following the exact standard format from the patent drafting template.
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import os

def set_cell_border(cell, **kwargs):
    """
    Set cell borders
    kwargs: top, bottom, left, right
    values: dict(sz=12, val='single', color='000000', space='0')
    """
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = tcPr.first_child_found_in("w:tcBorders")
    if tcBorders is None:
        tcBorders = OxmlElement('w:tcBorders')
        tcPr.append(tcBorders)
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        edge_data = kwargs.get(edge)
        if edge_data:
            tag = 'w:{}'.format(edge)
            element = tcBorders.find(qn(tag))
            if element is None:
                element = OxmlElement(tag)
                tcBorders.append(element)
            for key, val in edge_data.items():
                element.set(qn('w:{}'.format(key)), str(val))

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def create_patent_docx():
    doc = docx.Document()

    # Set page margins (1 inch all around)
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Base style
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(11)
    font.color.rgb = RGBColor(0, 0, 0)

    # Document Header Title
    header_p = doc.add_paragraph()
    header_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = header_p.add_run("PATENT APPLICATION DRAFT")
    r.bold = True
    r.font.size = Pt(16)
    r.font.name = 'Times New Roman'

    sub_p = doc.add_paragraph()
    sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = sub_p.add_run("Following information is required for drafting of patent application.")
    r_sub.italic = True
    r_sub.font.size = Pt(11)
    
    doc.add_paragraph() # Spacing

    # Helper function for section headings
    def add_section_heading(num_str, title_str):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        r_num = p.add_run(num_str + " ")
        r_num.bold = True
        r_num.font.size = Pt(12)
        r_title = p.add_run(title_str)
        r_title.bold = True
        r_title.font.size = Pt(12)
        return p

    # -------------------------------------------------------------
    # 1. Full name, nationality and address of applicant(s):
    # -------------------------------------------------------------
    add_section_heading("1.", "Full name, nationality and address of applicant(s):")
    
    table1 = doc.add_table(rows=3, cols=3)
    table1.alignment = WD_TABLE_ALIGNMENT.CENTER
    table1.autofit = False

    col_widths = [Inches(2.5), Inches(1.2), Inches(2.8)]
    headers1 = ["Full Name", "Nationality", "Address"]
    
    # Header Row
    hdr_cells = table1.rows[0].cells
    for i, name in enumerate(headers1):
        hdr_cells[i].text = name
        hdr_cells[i].paragraphs[0].runs[0].bold = True
        set_cell_background(hdr_cells[i], 'E0E0E0')

    # Data Rows
    data1 = [
        ("Vishwakarma Institute of Technology", "Indian", "666, Upper Indiranagar, Bibwewadi, Pune, Maharashtra, India – 411 037"),
        ("Vishwakarma University", "Indian", "Survey No 2, 3, 4, Kondhwa Main Rd, Laxmi Nagar, Betal Nagar, Kondhwa, Pune, Maharashtra, India - 411048")
    ]
    for row_idx, row_data in enumerate(data1):
        row_cells = table1.rows[row_idx + 1].cells
        for col_idx, text in enumerate(row_data):
            row_cells[col_idx].text = text

    # Set cell borders and widths
    for row in table1.rows:
        for i, cell in enumerate(row.cells):
            cell.width = col_widths[i]
            set_cell_border(cell, 
                            top=dict(sz=4, val='single', color='000000'),
                            bottom=dict(sz=4, val='single', color='000000'),
                            left=dict(sz=4, val='single', color='000000'),
                            right=dict(sz=4, val='single', color='000000'))

    doc.add_paragraph()

    # -------------------------------------------------------------
    # 2. Full name, nationality, address, mail id, and phone number of inventor(s):
    # -------------------------------------------------------------
    add_section_heading("2.", "Full name (including middle name), nationality, address, mail id, and phone number of inventor(s):")

    table2 = doc.add_table(rows=3, cols=5)
    table2.alignment = WD_TABLE_ALIGNMENT.CENTER
    table2.autofit = False
    
    col_widths2 = [Inches(1.5), Inches(0.6), Inches(2.2), Inches(1.4), Inches(0.8)]
    headers2 = ["Full Name (Including middle name)", "Nationality", "VIT Address (Start with full dept. name followed by full institute name)", "Mail ID", "Phone No."]

    hdr_cells2 = table2.rows[0].cells
    for i, name in enumerate(headers2):
        hdr_cells2[i].text = name
        hdr_cells2[i].paragraphs[0].runs[0].bold = True
        hdr_cells2[i].paragraphs[0].runs[0].font.size = Pt(9.5)
        set_cell_background(hdr_cells2[i], 'E0E0E0')

    data2 = [
        ("Prof. Vijaykumar Raghunath Ghule", "IN", "Department of Computer Science & Engineering (Data Science), Vishwakarma Institute of Technology, Pune", "Vijaykumar.ghule@vit.edu", "8624046893"),
        ("Sail Sitaram Nagale", "IN", "Department of Computer Science & Engineering (Data Science), Vishwakarma Institute of Technology, Pune", "sail.nagale@vit.edu", "")
    ]
    for row_idx, row_data in enumerate(data2):
        row_cells = table2.rows[row_idx + 1].cells
        for col_idx, text in enumerate(row_data):
            row_cells[col_idx].text = text
            row_cells[col_idx].paragraphs[0].runs[0].font.size = Pt(9.5)

    for row in table2.rows:
        for i, cell in enumerate(row.cells):
            cell.width = col_widths2[i]
            set_cell_border(cell, 
                            top=dict(sz=4, val='single', color='000000'),
                            bottom=dict(sz=4, val='single', color='000000'),
                            left=dict(sz=4, val='single', color='000000'),
                            right=dict(sz=4, val='single', color='000000'))

    doc.add_paragraph()

    # Signatures Table
    sig_p = doc.add_paragraph()
    sig_p.add_run("Copy and paste clear soft copy of signatures of all inventors in the following table: (Insert or delete the cells as per number of inventors)").italic = True
    
    table_sig = doc.add_table(rows=2, cols=4)
    table_sig.alignment = WD_TABLE_ALIGNMENT.CENTER
    table_sig.autofit = False
    
    sig_names = ["Vijaykumar Ghule", "Sail Sitaram Nagale", "Name 3", "Name 4"]
    for i, cell in enumerate(table_sig.rows[0].cells):
        cell.text = sig_names[i]
        cell.paragraphs[0].runs[0].bold = True
        set_cell_background(cell, 'F0F0F0')
    
    for cell in table_sig.rows[1].cells:
        cell.text = "\n\n(Signature)\n"

    for row in table_sig.rows:
        for cell in row.cells:
            cell.width = Inches(1.6)
            set_cell_border(cell, 
                            top=dict(sz=4, val='single', color='000000'),
                            bottom=dict(sz=4, val='single', color='000000'),
                            left=dict(sz=4, val='single', color='000000'),
                            right=dict(sz=4, val='single', color='000000'))

    doc.add_paragraph()

    # -------------------------------------------------------------
    # 3. Title of the invention:
    # -------------------------------------------------------------
    add_section_heading("3.", "Title of the invention:")
    p3 = doc.add_paragraph()
    p3.paragraph_format.left_indent = Inches(0.25)
    r = p3.add_run("IOT AND MACHINE LEARNING-BASED PREDICTIVE WORKER SAFETY HELMET WITH REAL-TIME HAZARD DETECTION")
    r.bold = True
    
    p3_note = doc.add_paragraph()
    p3_note.paragraph_format.left_indent = Inches(0.25)
    p3_note.add_run("(Word count: 14 words - Complies with limit of not more than 15 words)").italic = True

    # -------------------------------------------------------------
    # 4. Technical field of the invention:
    # -------------------------------------------------------------
    add_section_heading("4.", "Technical field of the invention:")
    p4 = doc.add_paragraph()
    p4.paragraph_format.left_indent = Inches(0.25)
    p4.add_run(
        "The present invention relates generally to industrial occupational safety systems, wearable embedded electronic devices, and edge computing. "
        "More specifically, the present invention relates to an Internet of Things (IoT) and Machine Learning (ML) enabled smart helmet system designed "
        "for continuous multi-modal environmental hazard detection, worker physiological biometric monitoring, 6-axis kinematic fall and impact detection, "
        "on-device predictive risk scoring, and dual-mode resilient wireless telemetry dispatch for construction, mining, and hazardous industrial sites."
    )

    # -------------------------------------------------------------
    # 5. Prior art:
    # -------------------------------------------------------------
    add_section_heading("5.", "Prior art:")
    p5 = doc.add_paragraph()
    p5.paragraph_format.left_indent = Inches(0.25)
    p5.add_run(
        "Conventional safety helmets used in construction and industrial sectors are passive structural headgear engineered solely for mechanical shock absorption. "
        "They are incapable of detecting invisible environmental hazards (toxic gases, elevated thermal exposure) or physiological collapse in workers.\n\n"
        "Recent electronic helmet systems incorporate individual sensors but suffer from critical shortcomings:\n"
        "1. Static Thresholding & High False Alarms: Existing devices trigger alarms based on instantaneous threshold breaches, failing to detect gradual pre-incident hazard accumulation or generating nuisance alarms.\n"
        "2. Lack of Predictive Multi-Sensor Fusion: Conventional systems do not correlate physiological metrics (heart rate) with ambient parameters (temperature, toxic gases) and kinematic vectors (acceleration magnitude, jerk).\n"
        "3. Cloud Dependency & Network Latency: Existing solutions rely on constant cloud connectivity for computational inference, rendering them ineffective in radio-shadowed environments like tunnels or deep basements.\n"
        "4. Absence of Integrated Geo-Telemetry: Inability to pinpoint exact coordinates of incapacitated workers during emergencies delays rescue intervention.\n\n"
        "The present invention overcomes all of the above disadvantages by executing on-device edge ML inference, dynamic feature extraction, predictive risk scoring (0-100), dual-action local/remote alarming, and hybrid LoRa/Wi-Fi telemetry with GPS tracking."
    )

    # -------------------------------------------------------------
    # 6. Objective(s) of Invention:
    # -------------------------------------------------------------
    add_section_heading("6.", "Objective(s) of Invention:")
    objectives = [
        "To provide a non-intrusive smart safety helmet that continuously monitors environmental hazards, worker biometrics, and kinematic motion in real time.",
        "To provide an edge computing architecture with an embedded machine learning model capable of computing a dynamic continuous Safety Risk Score (0–100) and classifying conditions into Low, Medium, and High Risk tiers.",
        "To reliably detect emergencies including sudden falls, high-g mechanical impacts, hazardous gas accumulation, elevated heat stress, and abnormal heart rates before fatal incidents occur.",
        "To implement a dual-mode low-latency emergency response mechanism comprising instant localized audiovisual alarms (<100 ms) and automated wireless telemetry dispatch to a supervisory dashboard.",
        "To incorporate geospatial coordinates via an onboard GPS receiver to enable immediate search-and-rescue localization across large-scale industrial infrastructures.",
        "To log multi-modal time-series safety records to a central database for retrospective incident analysis, compliance audits, and proactive workplace hazard mitigation."
    ]
    for obj in objectives:
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.left_indent = Inches(0.5)
        p.add_run(obj)

    # -------------------------------------------------------------
    # 7. Synopsis:
    # -------------------------------------------------------------
    add_section_heading("7.", "Synopsis:")
    p7 = doc.add_paragraph()
    p7.paragraph_format.left_indent = Inches(0.25)
    p7.add_run(
        "The present invention is an IoT and Machine Learning-enabled Predictive Worker Safety Helmet. "
        "The device comprises an industrial protective helmet shell (100) embedding a 32-bit dual-core microcontroller (101, ESP32 SoC), "
        "a temperature sensor (102), a toxic gas sensor (103), an optical photoplethysmography (PPG) heart rate sensor (104), "
        "a 6-axis Inertial Measurement Unit (105, MPU6050 accelerometer and gyroscope), a GPS receiver (106), "
        "an audiovisual alert module (107, piezoelectric buzzer and high-luminescence LED), and a hybrid wireless transceiver (108, Wi-Fi and sub-GHz LoRa), "
        "powered by a rechargeable power management circuit (109).\n\n"
        "The microcontroller samples multi-sensor feeds, applies edge noise filtering, and extracts dynamic statistical features (acceleration magnitude, jerk derivative, rate of temperature change, and gas concentration). "
        "A trained machine learning model running on the edge processor computes a real-time Risk Score (0–100). When the score exceeds predefined safety bounds or a critical fall/impact signature is recognized, "
        "the helmet immediately actuates local audiovisual warnings and dispatches an emergency telemetry packet containing worker ID, physiological vitals, and GPS coordinates to a central supervisory dashboard (111)."
    )

    # -------------------------------------------------------------
    # 8. Brief description of drawings:
    # -------------------------------------------------------------
    add_section_heading("8.", "Brief description of drawings (if any):")
    p8 = doc.add_paragraph()
    p8.paragraph_format.left_indent = Inches(0.25)
    p8.add_run(
        "Figure 1 illustrates the architectural block diagram and electrical hardware configuration of the predictive worker safety helmet system according to the present invention. Whereas:\n"
        "100 denotes smart helmet protective shell,\n"
        "101 denotes microcontroller and edge processing unit (ESP32 SoC),\n"
        "102 denotes temperature sensor module,\n"
        "103 denotes hazardous/toxic gas sensor module,\n"
        "104 denotes biometric PPG heart rate sensor,\n"
        "105 denotes 6-axis inertial measurement unit (IMU - MPU6050),\n"
        "106 denotes global positioning system (GPS) module,\n"
        "107 denotes audiovisual warning unit (piezoelectric buzzer and alert LED),\n"
        "108 denotes hybrid wireless telemetry interface (Wi-Fi / LoRa),\n"
        "109 denotes rechargeable power management and battery unit,\n"
        "110 denotes cloud server and central database repository,\n"
        "111 denotes supervisory IoT monitoring dashboard and safety terminal.\n\n"
        "Figure 2 illustrates the machine learning predictive risk assessment and emergency alert execution pipeline. Whereas:\n"
        "200 denotes multi-sensor real-time data acquisition stage,\n"
        "201 denotes edge data cleaning and noise filtering stage,\n"
        "202 denotes dynamic feature extraction engine,\n"
        "203 denotes machine learning predictive risk assessment engine (trained model),\n"
        "204 denotes risk scoring (0–100) and tri-level classification logic,\n"
        "205 denotes dual-action local warning and cloud telemetry dispatch module."
    )

    # -------------------------------------------------------------
    # 9. Detailed description of the invention:
    # -------------------------------------------------------------
    add_section_heading("9.", "Detailed description of the invention:")
    p9 = doc.add_paragraph()
    p9.paragraph_format.left_indent = Inches(0.25)
    p9.add_run(
        "Referring to Figure 1, the hardware assembly comprises an industrial thermoplastic helmet shell (100) enclosing an electronic processing core (101). "
        "The sensing suite includes an internal/ambient temperature sensor (102), a hazardous gas sensor (103, detecting CO, CH4, H2S, and LPG), "
        "a skin-contact PPG pulse sensor (104) mounted on the inner headband, a 6-axis IMU (105, MPU6050) rigidly attached to the helmet apex, "
        "and a GPS module (106) with a ceramic patch antenna. The device is powered by a protected Li-Po battery unit (109).\n\n"
        "Referring to Figure 2, the operational pipeline executes the following stages:\n"
        "1. Data Acquisition (200) & Noise Filtering (201): The IMU is polled at 50 Hz, biometric sensor at 20 Hz, and gas/temperature at 1 Hz. Median and moving average filters suppress spikes and motion artifacts.\n"
        "2. Dynamic Feature Extraction (202): Computes total acceleration magnitude Amag(t) = sqrt(ax^2 + ay^2 + az^2), jerk derivative J(t) = d(Amag)/dt, moving average heart rate, temperature rate-of-change (dT/dt), and gas concentration slope.\n"
        "3. Predictive Machine Learning Engine (203, 204): A trained Random Forest / Decision Tree model evaluates the dynamic feature vector and computes a normalized Safety Risk Score R(t) in [0, 100]. The score is classified into:\n"
        "   - Low Risk (0 <= R < 40): Normal operational condition. Telemetry logged periodically.\n"
        "   - Medium Risk (40 <= R < 75): Pre-hazardous advisory state. Intermittent alert activated; advisory flagged to dashboard.\n"
        "   - High Risk (75 <= R <= 100): Critical emergency (e.g., fall signature J > 25 g/s followed by immobility, acute gas leak > 50 PPM, severe cardiac distress). Continuous local alarm triggered.\n"
        "4. Dual-Action Alert & Telemetry (205): The helmet immediately drives buzzer and LED (107) and transmits an emergency JSON telemetry packet via Wi-Fi or LoRa (108) to the supervisory dashboard (111) with exact GPS coordinates."
    )

    # -------------------------------------------------------------
    # 10. Best method of performance of the invention:
    # -------------------------------------------------------------
    add_section_heading("10.", "Best method of performance of the invention:")
    p10 = doc.add_paragraph()
    p10.paragraph_format.left_indent = Inches(0.25)
    p10.add_run(
        "In practical deployment, a worker equips the helmet (100) and switches on the power unit (109). The microcontroller (101) performs an automated self-diagnostic check on all sensors (102-106), "
        "emits a confirmation beep via buzzer (107), and connects to the local LoRa gateway / Wi-Fi network (108).\n\n"
        "During work operations, the IMU (105) continuously tracks head kinematics at 50 Hz while the PPG sensor (104) monitors cardiac response. "
        "If a worker loses balance and falls from height, the IMU records free-fall weightlessness followed by an impact shock (>3.5g) and subsequent motionless state. "
        "Concurrently, if toxic gas levels rise (e.g., CO > 35 PPM) while ambient temperature reaches 40°C, the ML model detects the compound hazard pattern and escalates the Risk Score to 95 (High Risk). "
        "Within 80 milliseconds, the local 90 dB buzzer and high-intensity LED (107) actuate, while an emergency LoRa packet containing the worker ID, biometric vitals, and GPS location is broadcast to the supervisory dashboard (111), "
        "enabling rescue teams to pinpoint and extract the worker within minutes."
    )

    # -------------------------------------------------------------
    # 11. CLAIMS:
    # -------------------------------------------------------------
    add_section_heading("11.", "CLAIMS:")
    p11_lead = doc.add_paragraph()
    p11_lead.paragraph_format.left_indent = Inches(0.25)
    p11_lead.add_run("We Claim:").bold = True

    claims = [
        "1. An IoT and machine learning-enabled predictive worker safety helmet system comprising:\n"
        "a protective helmet shell (100) configured to be worn by an industrial worker;\n"
        "an environmental sensing unit including a temperature sensor (102) and a hazardous gas sensor (103) attached to said helmet shell;\n"
        "a biometric sensing unit comprising a photoplethysmography (PPG) heart rate sensor (104) positioned to maintain contact with the worker's skin;\n"
        "a kinematic sensing unit comprising a 6-axis inertial measurement unit (IMU) (105) including a 3-axis accelerometer and a 3-axis gyroscope;\n"
        "a geospatial positioning unit comprising a global positioning system (GPS) module (106);\n"
        "an audiovisual warning unit (107) comprising an acoustic buzzer and a visual light emitting diode (LED);\n"
        "a wireless communication transceiver (108) supporting dual-mode Wi-Fi and Long Range (LoRa) telemetry; and\n"
        "a microcontroller and edge processing unit (101) communicatively coupled to said sensors, warning unit, and wireless transceiver, wherein said edge processing unit is configured to extract multi-modal feature vectors from real-time sensor data, compute a predictive safety risk score (0 to 100) using an embedded machine learning model (203), categorize said score into a plurality of risk levels (204), and autonomously actuate said audiovisual warning unit (107) and transmit emergency telemetry packets to a supervisory dashboard (111) upon detection of a hazardous condition.",

        "2. The system as claimed in claim 1, wherein said machine learning model (203) is trained on historical multi-modal industrial sensor data and evaluates an input feature vector comprising instantaneous acceleration magnitude, dynamic jerk derivative, moving average heart rate, rate of temperature increase, and toxic gas concentration to predict potential safety incidents before threshold failure.",

        "3. The system as claimed in claim 1, wherein said edge processing unit (101) is configured with a tri-level risk classification logic comprising a Low Risk level (0 <= R < 40) signifying normal operational parameters, a Medium Risk level (40 <= R < 75) triggering an advisory alert on said supervisory dashboard and intermittent local warning, and a High Risk level (75 <= R <= 100) triggering continuous local acoustic and visual alarms and instantaneous transmission of emergency geospatial and physiological payloads.",

        "4. The system as claimed in claim 1, wherein said kinematic sensing unit (105) executes a fall and collision detection routine configured to identify a free-fall acceleration signature followed by a high-g impact peak exceeding a defined acceleration threshold and a subsequent zero-motion window.",

        "5. The system as claimed in claim 1, wherein said hazardous gas sensor (103) is configured to detect one or more toxic and flammable gases selected from the group consisting of Carbon Monoxide (CO), Methane (CH4), Hydrogen Sulfide (H2S), and Liquefied Petroleum Gas (LPG).",

        "6. The system as claimed in claim 1, wherein said wireless communication transceiver (108) is configured with automated failover logic to transmit emergency packets over LoRa frequencies when local Wi-Fi network connectivity is unavailable.",

        "7. The system as claimed in claim 1, wherein said emergency telemetry packet transmitted to said supervisory dashboard (111) comprises worker identification code, real-time GPS coordinates, time stamp, current heart rate, ambient gas concentration, helmet temperature, and current predictive risk score.",

        "8. A computer-implemented method for predictive occupational safety monitoring using a smart helmet, comprising the steps of:\n"
        "acquiring continuous time-synchronized data streams from a multi-sensor array comprising temperature, gas, heart rate, 6-axis IMU, and GPS sensors;\n"
        "filtering raw sensor data to eliminate high-frequency noise and motion artifacts;\n"
        "extracting dynamic temporal and kinematic features from the filtered sensor data;\n"
        "executing an embedded machine learning predictive risk assessment algorithm on the extracted features to generate a normalized numerical risk score from 0 to 100;\n"
        "comparing said risk score against defined safety classification thresholds;\n"
        "energizing a local audiovisual alert unit on the helmet when the risk score exceeds a predetermined threshold; and\n"
        "transmitting an emergency telemetry packet containing geospatial location and physiological metrics over a wireless interface to a remote monitoring dashboard for emergency response coordination."
    ]

    for c in claims:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Inches(0.25)
        p.paragraph_format.space_after = Pt(6)
        p.add_run(c)

    # -------------------------------------------------------------
    # 12. Inventive step of your invention:
    # -------------------------------------------------------------
    add_section_heading("12.", "Inventive step of your invention:")
    p12 = doc.add_paragraph()
    p12.paragraph_format.left_indent = Inches(0.25)
    p12.add_run(
        "The inventive step of the present invention resides in the technical convergence of:\n"
        "1. Multi-Modal Predictive Sensor Fusion vs. Static Thresholding: Instead of relying on isolated point-in-time threshold triggers, the invention dynamically correlates multi-channel physiological, environmental, and kinematic variables through an edge-optimized ML model, detecting evolving pre-incident hazards (e.g., heat stress combined with toxic gas inhalation) before worker incapacitation.\n"
        "2. On-Device Edge Processing & Sub-Second Latency: Embedding the feature extraction and classification model directly on the microcontroller (101) guarantees instantaneous local warning actuation without relying on cloud availability or suffering network delays.\n"
        "3. Resilient Dual-Mode Wireless Telemetry & Integrated GPS: Combining Wi-Fi with sub-GHz LoRa modulation ensures reliable emergency data transmission across deep construction trenches, tunnels, and remote industrial complexes alongside precise GPS coordinates."
    )

    # -------------------------------------------------------------
    # 13. Industrial application:
    # -------------------------------------------------------------
    add_section_heading("13.", "Industrial application:")
    p13 = doc.add_paragraph()
    p13.paragraph_format.left_indent = Inches(0.25)
    p13.add_run(
        "The present invention has direct industrial utility across multiple hazardous sectors:\n"
        "• Civil Construction and Infrastructure: Real-time detection of falls from scaffolds, crane zone collisions, and heat exhaustion.\n"
        "• Mining and Tunneling: Continuous monitoring of toxic and explosive gas buildup (CO, CH4, H2S), asphyxiation risks, and worker entrapment.\n"
        "• Petrochemical Refineries & Chemical Plants: Early warning for volatile chemical leaks, excessive thermal proximity, and worker distress.\n"
        "• Heavy Manufacturing, Foundries & Metallurgy: Heat stress indexing and impact monitoring in high-temperature blast furnace zones.\n"
        "• Firefighting and Disaster Rescue: Real-time physiological tracking and geospatial tracing of emergency personnel in obscured environments."
    )

    # -------------------------------------------------------------
    # 14. Abstract:
    # -------------------------------------------------------------
    add_section_heading("14.", "Abstract:")
    p14 = doc.add_paragraph()
    p14.paragraph_format.left_indent = Inches(0.25)
    p14.add_run(
        "An IoT and machine learning-enabled predictive worker safety helmet and method are disclosed for real-time hazard detection and proactive occupational safety monitoring. "
        "The smart helmet comprises an industrial helmet shell (100) integrating a microcontroller unit (101), a temperature sensor (102), a hazardous gas sensor (103), "
        "a photoplethysmography heart rate sensor (104), a 6-axis inertial measurement unit (105), a GPS module (106), an audiovisual alarm (107), and a dual-mode wireless communication module (108). "
        "The edge microcontroller continuously samples multi-modal sensor feeds, removes artifacts, extracts dynamic features, and executes an onboard machine learning model (203) to compute a real-time risk score (0–100) "
        "categorized into low, medium, and high risk levels. Upon detecting hazardous events—such as falls, toxic gas leaks, excessive thermal stress, or cardiac irregularities—the helmet instantly actuates local alarms "
        "and dispatches emergency telemetry packets containing exact GPS coordinates to a central supervisory dashboard (111) for rapid rescue intervention."
    )

    # -------------------------------------------------------------
    # 15. Drawing:
    # -------------------------------------------------------------
    add_section_heading("15.", "Drawing:")
    
    p15_note = doc.add_paragraph()
    p15_note.paragraph_format.left_indent = Inches(0.25)
    p15_note.add_run("Drawings must not be labeled anywhere with text descriptions. Only single numerals (100-111, 200-205) are used to denote components as described in Section 8.").italic = True

    # Drawing Figures Text Representation
    p_fig1 = doc.add_paragraph()
    p_fig1.paragraph_format.left_indent = Inches(0.25)
    r_f1 = p_fig1.add_run("Figure 1: Hardware Architecture & Subsystems Block Diagram")
    r_f1.bold = True
    
    fig1_text = (
        "+-----------------------------------------------------------------------------------+\n"
        "|                        SMART HELMET ENCLOSURE (100)                               |\n"
        "|                                                                                   |\n"
        "|  +--------------------+  +--------------------+  +-----------------------------+  |\n"
        "|  | Temperature Sensor |  | Toxic Gas Sensor   |  | Heart Rate (PPG) Sensor     |  |\n"
        "|  | (102)              |  | (103)              |  | (104)                       |  |\n"
        "|  +---------+----------+  +---------+----------+  +--------------+--------------+  |\n"
        "|            |                       |                            |                 |\n"
        "|            +-----------------------+----------------------------+                 |\n"
        "|                                    |                                              |\n"
        "|  +--------------------+            v             +-----------------------------+  |\n"
        "|  | 6-Axis IMU (MPU6050)| ---> [ MICROCONTROLLER ] <---| GPS Module (106)       |  |\n"
        "|  | (105)              |     [ & EDGE PROCESSOR ] |                             |  |\n"
        "|  +--------------------+     [ (ESP32 SoC) (101)] +-----------------------------+  |\n"
        "|                                    |                                              |\n"
        "|            +-----------------------+----------------------------+                 |\n"
        "|            |                       |                            |                 |\n"
        "|            v                       v                            v                 |\n"
        "|  +--------------------+  +--------------------+  +-----------------------------+  |\n"
        "|  | Audiovisual Alert  |  | Hybrid Transceiver |  | Power Regulation & Battery  |  |\n"
        "|  | (Buzzer & LED)(107)|  | (Wi-Fi/LoRa) (108) |  | (109)                       |  |\n"
        "|  +--------------------+  +---------+----------+  +-----------------------------+  |\n"
        "+------------------------------------|----------------------------------------------+\n"
        "                                     | (Wireless Telemetry)\n"
        "                                     v\n"
        "                  +--------------------------------------+\n"
        "                  | Cloud Server & Central Database (110)|\n"
        "                  +------------------+-------------------+\n"
        "                                     |\n"
        "                                     v\n"
        "                  +--------------------------------------+\n"
        "                  | Supervisory Monitoring Dashboard     |\n"
        "                  | & Safety Officer Terminal (111)      |\n"
        "                  +--------------------------------------+\n"
        "                                 Figure 1"
    )
    p_f1_box = doc.add_paragraph()
    p_f1_box.paragraph_format.left_indent = Inches(0.25)
    r_code1 = p_f1_box.add_run(fig1_text)
    r_code1.font.name = 'Courier New'
    r_code1.font.size = Pt(8.5)

    doc.add_paragraph()

    p_fig2 = doc.add_paragraph()
    p_fig2.paragraph_format.left_indent = Inches(0.25)
    r_f2 = p_fig2.add_run("Figure 2: Machine Learning Risk Assessment & Alert Pipeline")
    r_f2.bold = True

    fig2_text = (
        "+-----------------------------------------------------------------------------------+\n"
        "|   +---------------------------------------------------------------------------+   |\n"
        "|   | (200) Multi-Sensor Data Acquisition: Temperature, Gas, HR, IMU, GPS       |   |\n"
        "|   +-------------------------------------+-------------------------------------+   |\n"
        "|                                         |                                         |\n"
        "|                                         v                                         |\n"
        "|   +---------------------------------------------------------------------------+   |\n"
        "|   | (201) Edge Preprocessing: Noise Filtering, Normalization, Spike Removal   |   |\n"
        "|   +-------------------------------------+-------------------------------------+   |\n"
        "|                                         |                                         |\n"
        "|                                         v                                         |\n"
        "|   +---------------------------------------------------------------------------+   |\n"
        "|   | (202) Feature Extraction: Accel Magnitude, Jerk, HR Variability, Gas Rate |   |\n"
        "|   +-------------------------------------+-------------------------------------+   |\n"
        "|                                         |                                         |\n"
        "|                                         v                                         |\n"
        "|   +---------------------------------------------------------------------------+   |\n"
        "|   | (203) ML Predictive Model: Random Forest / Gradient Boosted Inference     |   |\n"
        "|   +-------------------------------------+-------------------------------------+   |\n"
        "|                                         |                                         |\n"
        "|                                         v                                         |\n"
        "|   +---------------------------------------------------------------------------+   |\n"
        "|   | (204) Risk Score Calculation (0-100) & Tri-Level Classification:          |   |\n"
        "|   |       • Low Risk (0-39)    --> Routine Periodic Log                       |   |\n"
        "|   |       • Medium Risk (40-74)--> Precautionary Advisory                     |   |\n"
        "|   |       • High Risk (75-100) --> Immediate Emergency Alarm                  |   |\n"
        "|   +-------------------------------------+-------------------------------------+   |\n"
        "|                                         |                                         |\n"
        "|                                         v                                         |\n"
        "|   +---------------------------------------------------------------------------+   |\n"
        "|   | (205) Dual Action Dispatch: Local Buzzer/LED (107) + Remote Cloud/LoRa    |   |\n"
        "|   |       Alert to Supervisory Dashboard (111) with GPS Coordinates           |   |\n"
        "|   +---------------------------------------------------------------------------+   |\n"
        "+-----------------------------------------------------------------------------------+\n"
        "                                 Figure 2"
    )
    p_f2_box = doc.add_paragraph()
    p_f2_box.paragraph_format.left_indent = Inches(0.25)
    r_code2 = p_f2_box.add_run(fig2_text)
    r_code2.font.name = 'Courier New'
    r_code2.font.size = Pt(8.5)

    # Save Word document
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Patent_Draft_Predictive_Worker_Safety_Helmet.docx")
    doc.save(output_path)
    print(f"Successfully generated Word (.docx) document at: {output_path}")

if __name__ == '__main__':
    create_patent_docx()
