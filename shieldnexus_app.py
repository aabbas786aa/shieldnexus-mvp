

# Simulated AI Matching Logic
def simulate_shieldinsights_trigger(use_case):
    # For demo purposes, always return vendors we have profiles for
    return ["TrustLock", "CyberSentinel", "SkyArmor"]



# ShieldNexus.ai MVP – With Export, Admin View, Tooltips, Customer & Vendor Tracking

import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import io
import random
import plotly.express as px

# ---------------- Dark Mode Theme Setup ----------------
mpl.rcParams.update({
    "axes.facecolor": "#1e1e1e",
    "axes.edgecolor": "white",
    "axes.labelcolor": "white",
    "figure.facecolor": "#1e1e1e",
    "text.color": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "axes.titlecolor": "white",
    "axes.titleweight": "bold",
    "axes.titlesize": 14,
    "grid.color": "#444444",
})
sns.set_style("darkgrid")

st.set_page_config(layout="centered", page_title="ShieldNexus.ai | Vendor Intelligence Hub")

# ---------------- Header & Branding ----------------
st.markdown("""
    <h1 style='text-align: center; color: #4FC3F7;'>ShieldNexus.ai</h1>
    <h4 style='text-align: center; color: #ccc;'>AI-Powered Cybersecurity Vendor Intelligence & Execution Hub</h4>
    <hr style='margin-top:10px;margin-bottom:30px;'>
""", unsafe_allow_html=True)

# ---------------- Login Role Selection ----------------
st.subheader("Choose Login Type")
login_type = st.radio("Select your role:", ["Customer (CISO Team)", "Vendor (Security Provider)", "Admin View"])

if "user_type" not in st.session_state:
    st.session_state["user_type"] = None
if "admin_logs" not in st.session_state:
    st.session_state["admin_logs"] = []
if "vendor_grc_data" not in st.session_state:
    st.session_state["vendor_grc_data"] = pd.DataFrame({
        "Control Area": ["Access Management", "Encryption", "Logging & Monitoring", "Incident Response", "Third Party Risk", "Endpoint Protection"],
        "Gap Status": ["Open", "Resolved", "In Progress", "Open", "Resolved", "In Progress"],
        "Assigned To": ["IT Ops", "Security Lead", "GRC Analyst", "SOC Team", "Compliance Officer", "IT Ops"],
        "Due Date": ["2025-04-10", "2025-03-29", "2025-04-15", "2025-04-20", "2025-03-25", "2025-04-30"],
        "Evidence Uploaded": ["No", "Yes", "Partial", "No", "Yes", "Partial"]
    })

# ---------------- AI Matching Function ----------------

    # ---------------- AI Matching Function ----------------

def simulate_shieldinsights_trigger(use_case):
    # For demo purposes, always return vendors we have profiles for
    if use_case == "M&A Integration Support":
        return ["TrustLock", "CyberSentinel", "SkyArmor"]
    elif use_case == "IAM Remediation":
        return ["CloudSentinel", "TrustWare"]
    elif use_case == "Cloud Security Hardening":
        return ["SkyFence", "NetArmor"]
    else:
        return ["TrustWare", "SecureEdge"]

# ---------------- CUSTOMER WORKFLOW ----------------
# ---------------- CUSTOMER WORKFLOW ----------------
if login_type == "Customer (CISO Team)":
    st.session_state["user_type"] = "customer"
    st.header("🤝 From ShieldInsights.ai to ShieldNexus.ai")
    st.markdown("""
    <div style='background-color: #263238; padding: 10px 20px; border-radius: 10px;'>
        <p style='color: #ccc;'>
            <strong>AI Insights Identified by ShieldInsights.ai</strong> have triggered a workflow to intelligently match your needs with vetted cybersecurity vendors inside ShieldNexus.ai.
            <br><br>
            This handoff is based on contextual understanding of your security gaps, use case priority, and organizational posture. Let’s review the top recommendations.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎯 Select Your Use Case")
    use_case = st.selectbox("Use Case Triggered from ShieldInsights.ai", [
        "M&A Integration Support",
        "IAM Remediation",
        "Cloud Security Hardening",
        "Third-Party Risk Management"])

    matched_vendors = simulate_shieldinsights_trigger(use_case)

    st.subheader("🔍 AI-Matched Vendors")
    vendor_df = pd.DataFrame({
        "Vendor Name": matched_vendors,
        "Capability Match": ["IAM, GRC", "Cloud, IAM", "GRC, Risk Mgmt"][:len(matched_vendors)],
        "Composite Score": [91, 88, 84][:len(matched_vendors)],
        "Risk Level": ["Low", "Medium", "Medium"][:len(matched_vendors)],
        "Reputation Score": [95, 89, 86][:len(matched_vendors)]
    })

    def make_link(vendor):
        profile_map = {
            "TrustLock": "https://shieldnexus-mvp-integration-shieldinsights.streamlit.app/#trustlock-profile",
            "CyberSentinel": "https://shieldnexus-mvp-integration-shieldinsights.streamlit.app/#cybersentinel-profile",
            "SkyArmor": "https://shieldnexus-mvp-integration-shieldinsights.streamlit.app/#skyarmor-profile",
        }
        if vendor in profile_map:
            return f"<a href='{profile_map[vendor]}' target='_blank'>{vendor}</a>"
        return vendor

    vendor_df["Vendor Profile"] = vendor_df["Vendor Name"].apply(lambda x: make_link(x))

    st.markdown("""
    <style>
    table td a { color: #4FC3F7; font-weight: bold; text-decoration: none; }
    </style>
    """, unsafe_allow_html=True)

st.markdown(vendor_df.to_html(escape=False, index=False), unsafe_allow_html=True)

   

    # ---------------- Anchor Sections for Vendor Profiles ----------------
    st.markdown("<h2 id='trustlock-profile'>🔍 TrustLock (MSSP)</h2>", unsafe_allow_html=True)
    st.markdown("**Risk Score:** 82 | **Reputation:** 90 | **Certifications:** SOC 2, ISO 27001")
    st.info("Minor encryption gap. Excellent reputation in financial sector.")

    st.markdown("<h2 id='cybersentinel-profile'>🔍 CyberSentinel (Software)</h2>", unsafe_allow_html=True)
    st.markdown("**Risk Score:** 67 | **Reputation:** 80 | **Certifications:** HIPAA, SOC 2")
    st.info("Patch management automation pending. No active exposure detected.")

    st.markdown("<h2 id='skyarmor-profile'>🔍 SkyArmor (Platform)</h2>", unsafe_allow_html=True)
    st.markdown("**Risk Score:** 91 | **Reputation:** 70 | **Certifications:** ISO 27001, FedRAMP (Pending)")
    st.warning("Multiple legacy ports exposed. Rapid remediation in progress.")

    # Optional JS to scroll to anchor if needed
    st.markdown("""
    <script>
    const hash = window.location.hash;
    if (hash) {
        const target = document.querySelector(hash);
        if (target) {
            target.scrollIntoView({behavior: "smooth"});
        }
    }
    </script>
    """, unsafe_allow_html=True)

    selected_vendor = st.selectbox("📋 Choose vendor to export report:", vendor_df["Vendor Name"])
    if st.button("📥 Export Vendor Report"):
        output = io.BytesIO()
        vendor_df[vendor_df["Vendor Name"] == selected_vendor].to_excel(output, index=False)
        st.download_button("Download Excel Report", data=output.getvalue(), file_name=f"{selected_vendor}_report.xlsx")
        st.session_state["admin_logs"].append({"User Type": "Customer", "Action": f"Exported report: {selected_vendor}", "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

    st.subheader("📅 Engagement Timeline View")
    timeline_data = pd.DataFrame({
        "Milestone": ["Engagement Start", "Security Assessment", "Solution Design", "Implementation", "Testing", "Go Live"],
        "Start": ["2025-04-01", "2025-04-03", "2025-04-07", "2025-04-14", "2025-04-18", "2025-04-24"],
        "Finish": ["2025-04-02", "2025-04-06", "2025-04-13", "2025-04-17", "2025-04-23", "2025-04-30"],
        "Owner": ["ShieldNexus", "Vendor", "Joint", "Vendor", "Customer", "Customer"]
    })
    fig = px.timeline(
        timeline_data,
        x_start="Start",
        x_end="Finish",
        y="Milestone",
        color="Owner",
        title="Customer Project Timeline",
        template="plotly_dark"
    )
    fig.update_yaxes(autorange="reversed")
    st.plotly_chart(fig, use_container_width=True)

# ---------------- VENDOR WORKFLOW ----------------
if login_type == "Vendor (Security Provider)":
    st.session_state["user_type"] = "vendor"
    st.header("📝 TRPR Submission Form")
    st.markdown("Enter security profile to trigger Risk Cognizance enrichment scan")

    col1, col2 = st.columns(2)
    with col1:
        mfa = st.selectbox("Is MFA Enabled?", ["Yes", "No"])
        pentest = st.selectbox("Recent Penetration Test?", ["Yes", "No"])
        dlp = st.text_input("DLP Tool/Practices")
    with col2:
        certs = st.multiselect("Certifications", ["SOC 2", "ISO 27001", "HIPAA", "PCI DSS"])
        domain = st.text_input("Official Domain")

    if st.button("🚀 Submit & Simulate Enrichment"):
        st.success("Risk Cognizance API Scan Triggered")

        rc_results = {
            "Dark Web Hits": random.randint(0, 5),
            "SSL Certificate Expiry (days)": random.randint(10, 90),
            "Exposed Services": random.sample(["SSH", "RDP", "SMTP", "Telnet"], 2),
            "Critical Vulnerabilities": random.randint(0, 10),
            "Reputation Score": random.randint(60, 95)
        }

        st.subheader("🔍 Simulated Risk Cognizance Results")
        st.json(rc_results)

        st.subheader("📊 Composite Scorecard")
        score_df = pd.DataFrame({
            "Metric": ["Reputation Score", "Vuln Risk", "Exposure Level"],
            "Score": [rc_results["Reputation Score"], 100 - rc_results["Critical Vulnerabilities"] * 7, 100 - rc_results["Dark Web Hits"] * 10]
        })
        fig, ax = plt.subplots(figsize=(6,3))
        sns.barplot(data=score_df, x="Score", y="Metric", palette="coolwarm", ax=ax)
        ax.set_xlim(0, 100)
        ax.set_title("Composite Risk Breakdown")
        st.pyplot(fig)

        st.subheader("🧠 AI Recommendations")
        st.markdown("- Mitigate exposed services: SSH, RDP")
        st.markdown("- Renew SSL certificates expiring soon")
        st.markdown("- Improve DLP enforcement and encryption standards")

    st.subheader("📤 Submit Final Compliance Package")
    st.markdown("After completing your GRC inputs and enrichment, you may now submit your compliance profile for admin and client review.")

    submitted_doc = st.file_uploader("📎 Upload Final Report / Documentation", type=["pdf", "xlsx", "csv", "zip"])
    if submitted_doc and st.button("✅ Submit to Admin"):
        st.success("Submission successful. Admin has been notified.")
        st.session_state["admin_logs"].append({
            "User Type": "Vendor",
            "Action": f"Submitted package: {submitted_doc.name}",
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
# ---------------- ADMIN WORKFLOW ----------------
if login_type == "Admin View":
    st.session_state["user_type"] = "admin"
    st.header("🧭 ShieldNexus Admin Console")

    admin_tabs = st.tabs([
    "Dashboard Overview",
    "Vendor Intelligence Hub",
    "Compliance Heatmap",
    "Risk Monitoring",
    "Vendor Profiles"  # New tab!
])


    # --------- TAB 1: DASHBOARD OVERVIEW ---------
    with admin_tabs[0]:
        st.markdown("### 📊 Dashboard Overview")
        st.markdown("<hr style='margin-top:-10px; margin-bottom:20px;'>", unsafe_allow_html=True)

        # ---- Sample Vendor Data ----
        vendor_data = pd.DataFrame({
            "Vendor Name": [
                "TrustLock", "CyberSentinel", "SkyArmor", "RiskProof",
                "FortiTech", "BreachZero", "DataShield", "NetWall"
            ],
            "Type": [
                "MSSP", "Software", "Platform", "Systems Integrator",
                "MSSP", "Implementation", "Software", "Platform"
            ],
            "Status": [
                "Qualified", "Pending", "Qualified", "Rejected",
                "Pending", "Qualified", "Pending", "Qualified"
            ],
            "Risk Score": [82, 67, 91, 45, 60, 85, 70, 88]
        })

        # ---- KPI Cards ----
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Vendors", len(vendor_data))
        with col2:
            st.metric("Qualified", (vendor_data["Status"] == "Qualified").sum())
        with col3:
            st.metric("Pending Vetting", (vendor_data["Status"] == "Pending").sum())
        with col4:
            avg_risk = vendor_data["Risk Score"].mean()
            st.metric("Avg Risk Score", f"{avg_risk:.1f}")

        # ---- Vendor Type Filter ----
        vendor_type_filter = st.selectbox(
            "Filter by Vendor Type",
            options=["All"] + sorted(vendor_data["Type"].unique().tolist())
        )

        filtered_data = vendor_data if vendor_type_filter == "All" else vendor_data[vendor_data["Type"] == vendor_type_filter]

        # ---- Pie Chart: Vendor Type Breakdown ----
        pie_data = vendor_data["Type"].value_counts().reset_index()
        pie_data.columns = ["Vendor Type", "Count"]
        fig = px.pie(pie_data, names="Vendor Type", values="Count", title="Vendor Type Breakdown", template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("<hr style='margin-top:-10px; margin-bottom:20px;'>", unsafe_allow_html=True)
        # ---- Bar Chart: Risk Score Distribution ----
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(vendor_data["Risk Score"], bins=10, kde=True, ax=ax)
        ax.set_title("Risk Score Distribution")
        ax.set_xlabel("Risk Score")
        ax.set_ylabel("Frequency")
        st.pyplot(fig)
        st.markdown("<hr style='margin-top:-10px; margin-bottom:20px;'>", unsafe_allow_html=True)
        # ---- Recent Activity ----
        st.subheader("📰 Recent Activity")

    
    # Your existing code...
    # --------- TAB 2: VENDOR INTELLIGENCE HUB ---------
    with admin_tabs[1]:
        st.markdown("### 🧠 Vendor Intelligence Hub")
        st.markdown("Manage, filter, and monitor vendors in real-time.")
    
        # Filters
        st.subheader("🔍 Filters")
        col1, col2, col3 = st.columns(3)
        with col1:
            filter_type = st.selectbox("Vendor Type", ["All"] + sorted(vendor_data["Type"].unique()))
        with col2:
            filter_status = st.selectbox("Status", ["All", "Qualified", "Pending", "Rejected"])
        with col3:
            risk_threshold = st.slider("Minimum Risk Score", 0, 100, 0)
    
        # Apply filters
        filtered = vendor_data.copy()
        if filter_type != "All":
            filtered = filtered[filtered["Type"] == filter_type]
        if filter_status != "All":
            filtered = filtered[filtered["Status"] == filter_status]
        filtered = filtered[filtered["Risk Score"] >= risk_threshold]
    
        # Add sample "Last Submitted" column for visual realism
        filtered["Last Submitted"] = pd.date_range(end=pd.Timestamp("today"), periods=len(filtered)).strftime("%Y-%m-%d")
    
        st.markdown("### 📋 Filtered Vendors")
        st.dataframe(filtered.style.format({"Risk Score": "{:.1f}"}))
    
        st.info(f"{len(filtered)} vendor(s) found. You can add export, view, and review actions here.")
        
        # -------- Charts to enhance visibility --------
        st.markdown("### 📊 Visual Insights")
        
        # 1. Vendor Count by Status
        status_counts = filtered["Status"].value_counts().reset_index()
        status_counts.columns = ["Status", "Count"]
        fig1 = px.bar(
            status_counts,
            x="Status",
            y="Count",
            color="Status",
            title="Vendors by Status",
            template="plotly_dark",
        )
        st.plotly_chart(fig1, use_container_width=True)
        
        # 2. Risk Score by Vendor Type (Box Plot)
        fig2 = px.box(
            filtered,
            x="Type",
            y="Risk Score",
            color="Type",
            title="Risk Score Distribution by Vendor Type",
            template="plotly_dark"
        )
        st.plotly_chart(fig2, use_container_width=True)
        
        # 3. Top 5 Riskiest Vendors
        top_risky = filtered.sort_values("Risk Score", ascending=True).head(5)
        fig3 = px.bar(
            top_risky,
            x="Risk Score",
            y="Vendor Name",
            orientation="h",
            color="Risk Score",
            title="Top 5 Riskiest Vendors",
            template="plotly_dark",
            color_continuous_scale="reds"
        )
        st.plotly_chart(fig3, use_container_width=True)
    
    # --------- TAB 3: COMPLIANCE HEATMAP ---------
    with admin_tabs[2]:
        st.markdown("### 🧯 Vendor Compliance Heatmap")
        st.markdown("Snapshot of vendor control posture (click export for deeper review).")
    
        vendors = ["TrustLock", "CyberSentinel", "SkyArmor", "RiskProof", "FortiTech"]
        controls = ["MFA", "Encryption", "Pen Testing", "DLP", "Incident Response"]
    
        status_options = ["Open", "In Progress", "Resolved"]
        status_colors = {"Open": "red", "In Progress": "yellow", "Resolved": "green"}
    
        import numpy as np
        heatmap_df = pd.DataFrame(
            np.random.choice(status_options, size=(len(vendors), len(controls))),
            index=vendors, columns=controls
        )
    
        # ---- Export Button ----
        st.subheader("📤 Export Compliance Matrix")
        import io


# Simulated AI Matching Logic

        output = io.BytesIO()
        heatmap_df.to_excel(output, index=True)
        st.download_button("Download Excel", output.getvalue(), file_name="compliance_heatmap.xlsx")
    
        # ---- Status Summary ----
        st.subheader("📌 Compliance Status Summary")
        all_statuses = heatmap_df.values.flatten()
        status_counts = pd.Series(all_statuses).value_counts()
        col1, col2, col3 = st.columns(3)
        col1.metric("Open", status_counts.get("Open", 0))
        col2.metric("In Progress", status_counts.get("In Progress", 0))
        col3.metric("Resolved", status_counts.get("Resolved", 0))
    
        # ---- Display Heatmap ----
        def color_map(val):
            return f'background-color: {status_colors.get(val, "white")}; color: black'
    
        st.subheader("🧮 Control Matrix View")
        st.dataframe(heatmap_df.style.applymap(color_map))

        
    # --------- TAB 4: RISK MONITORING ---------
    with admin_tabs[3]:
        st.markdown("### 🚨 Vendor Risk Monitoring")
        st.markdown("Monitor vendor risks across score distributions and critical outliers.")
    
        # Simulated extended data for interactive visuals
        vendor_risk_data = pd.DataFrame({
            "Vendor Name": [
                "TrustLock", "CyberSentinel", "SkyArmor", "RiskProof",
                "FortiTech", "BreachZero", "DataShield", "NetWall"
            ],
            "Type": [
                "MSSP", "Software", "Platform", "Systems Integrator",
                "MSSP", "Implementation", "Software", "Platform"
            ],
            "Risk Score": [82, 67, 91, 45, 60, 85, 70, 88],
            "Reputation Score": [90, 80, 70, 60, 75, 88, 69, 92]
        })
    
        # -- Chart 1: Risk Score Distribution by Vendor Type (Box Plot)
        st.subheader("📦 Risk Score Distribution by Vendor Type")
        fig1 = px.box(
            vendor_risk_data,
            x="Type",
            y="Risk Score",
            color="Type",
            template="plotly_dark",
            title="How Risk Varies Across Vendor Categories"
        )
        fig1.update_layout(hovermode="x unified")
        st.plotly_chart(fig1, use_container_width=True)
    
        # -- Chart 2: Risk Score vs Reputation Score (Scatter Plot)
        st.subheader("🎯 Risk Score vs Reputation Score")
        fig2 = px.scatter(
            vendor_risk_data,
            x="Reputation Score",
            y="Risk Score",
            color="Type",
            size="Risk Score",
            hover_name="Vendor Name",
            template="plotly_dark",
            title="Reputation vs Risk Landscape"
        )
        fig2.update_layout(hovermode="closest")
        st.plotly_chart(fig2, use_container_width=True)
    
        # -- Chart 3: Top 5 Riskiest Vendors (Bar Chart)
        st.subheader("🔥 Top 5 Riskiest Vendors")
        top5 = vendor_risk_data.sort_values(by="Risk Score", ascending=True).head(5)
        fig3 = px.bar(
            top5,
            x="Risk Score",
            y="Vendor Name",
            orientation="h",
            title="Who Are the Most At-Risk Vendors?",
            template="plotly_dark",
            color="Risk Score",
            color_continuous_scale="reds"
        )
        st.plotly_chart(fig3, use_container_width=True)
   
   # --------- TAB 5: VENDOR PROFILES ---------
    with admin_tabs[4]:
        st.markdown("### 🧾 Vendor Profiles")
        st.markdown("AI-generated security intelligence profiles based on internal and external data sources.")
    
        # 🔹 Shared Compliance Color Function
        def status_color(status):
            return {
                "Resolved": "#66bb6a",      # green
                "In Progress": "#fbc02d",   # yellow
                "Open": "#e53935"           # red
            }.get(status, "#aaa")
    
            # -------- TrustLock Profile --------
        with st.expander("🔍 TrustLock (MSSP)"):
                st.markdown("### 🛡️ TrustLock Overview")
                st.markdown("""
                <div style='padding:10px; background-color:#2c2c2c; border-radius:10px;'>
                TrustLock offers managed threat monitoring and 24/7 SOC services. Certified in SOC 2 and ISO 27001.
                </div>
                """, unsafe_allow_html=True)
        
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("#### 📈 Risk & Reputation")
                    st.metric(label="Risk Score", value="82")
                    st.metric(label="Reputation Score", value="90")
                with col2:
                    st.markdown("#### 🧪 Certifications")
                    st.markdown("- SOC 2 ✅")
                    st.markdown("- ISO 27001 ✅")
        
                st.markdown("#### 🧬 Risk Cognizance Enrichment")
                rc_cols = st.columns(3)
                rc_cols[0].markdown("🔍 **Dark Web Hits:**")
                rc_cols[0].markdown("<span style='color:red; font-weight:bold;'>1 match found</span>", unsafe_allow_html=True)
        
                rc_cols[1].markdown("⏳ **SSL Expiry:**")
                rc_cols[1].markdown("<span style='color:orange;'>22 days</span>", unsafe_allow_html=True)
        
                rc_cols[2].markdown("🐞 **Critical Vulns:**")
                rc_cols[2].markdown("<span style='color:red; font-weight:bold;'>3 found</span>", unsafe_allow_html=True)
        
                st.markdown("#### ✅ Compliance Summary")
                compliance_data_1 = {
                    "MFA": "Resolved",
                    "Encryption": "In Progress",
                    "Pen Testing": "Open"
                }
                comp_cols = st.columns(len(compliance_data_1))
                for idx, (control, status) in enumerate(compliance_data_1.items()):
                    comp_cols[idx].markdown(f"""
                    <div style='background-color:{status_color(status)}; padding:10px; border-radius:8px; text-align:center; color:black; font-weight:bold;'>
                    {control}<br>{status}
                    </div>
                    """, unsafe_allow_html=True)
        
                st.markdown("#### 📝 Notes")
                st.info("Minor encryption gap. Excellent reputation in financial sector.")
        
            # -------- CyberSentinel Profile --------
        with st.expander("🔍 CyberSentinel (Software)"):
                st.markdown("### 🧱 CyberSentinel Overview")
                st.markdown("""
                <div style='padding:10px; background-color:#2c2c2c; border-radius:10px;'>
                CyberSentinel builds next-gen endpoint security platforms tailored for regulated industries. HIPAA and SOC 2 certified.
                </div>
                """, unsafe_allow_html=True)
        
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("#### 📈 Risk & Reputation")
                    st.metric(label="Risk Score", value="67")
                    st.metric(label="Reputation Score", value="80")
                with col2:
                    st.markdown("#### 🧪 Certifications")
                    st.markdown("- HIPAA ✅")
                    st.markdown("- SOC 2 ✅")
        
                st.markdown("#### 🧬 Risk Cognizance Enrichment")
                rc_cols = st.columns(3)
                rc_cols[0].markdown("🔍 **Dark Web Hits:**")
                rc_cols[0].markdown("<span style='color:red; font-weight:bold;'>2 matches found</span>", unsafe_allow_html=True)
        
                rc_cols[1].markdown("⏳ **SSL Expiry:**")
                rc_cols[1].markdown("<span style='color:orange;'>40 days</span>", unsafe_allow_html=True)
        
                rc_cols[2].markdown("🐞 **Critical Vulns:**")
                rc_cols[2].markdown("<span style='color:red;'>5 found</span>", unsafe_allow_html=True)
        
                st.markdown("#### ✅ Compliance Summary")
                compliance_data_2 = {
                    "MFA": "Resolved",
                    "Encryption": "Resolved",
                    "Pen Testing": "In Progress"
                }
                comp_cols = st.columns(len(compliance_data_2))
                for idx, (control, status) in enumerate(compliance_data_2.items()):
                    comp_cols[idx].markdown(f"""
                    <div style='background-color:{status_color(status)}; padding:10px; border-radius:8px; text-align:center; color:black; font-weight:bold;'>
                    {control}<br>{status}
                    </div>
                    """, unsafe_allow_html=True)
        
                st.markdown("#### 📝 Notes")
                st.info("Patch management automation pending. No active exposure detected.")
        
            # -------- SkyArmor Profile --------
        with st.expander("🔍 SkyArmor (Platform)"):
                st.markdown("### ☁️ SkyArmor Overview")
                st.markdown("""
                <div style='padding:10px; background-color:#2c2c2c; border-radius:10px;'>
                SkyArmor delivers secure cloud orchestration layers and data isolation platforms for large-scale enterprises.
                </div>
                """, unsafe_allow_html=True)
        
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("#### 📈 Risk & Reputation")
                    st.metric(label="Risk Score", value="91")
                    st.metric(label="Reputation Score", value="70")
                with col2:
                    st.markdown("#### 🧪 Certifications")
                    st.markdown("- ISO 27001 ✅")
                    st.markdown("- FedRAMP (Pending) ⚠️")
        
                st.markdown("#### 🧬 Risk Cognizance Enrichment")
                rc_cols = st.columns(3)
                rc_cols[0].markdown("🔍 **Dark Web Hits:**")
                rc_cols[0].markdown("<span style='color:red;'>3 matches found</span>", unsafe_allow_html=True)
        
                rc_cols[1].markdown("⏳ **SSL Expiry:**")
                rc_cols[1].markdown("<span style='color:orange;'>15 days</span>", unsafe_allow_html=True)
        
                rc_cols[2].markdown("🐞 **Critical Vulns:**")
                rc_cols[2].markdown("<span style='color:red; font-weight:bold;'>7 found</span>", unsafe_allow_html=True)
        
                st.markdown("#### ✅ Compliance Summary")
                compliance_data_3 = {
                    "MFA": "In Progress",
                    "Encryption": "Resolved",
                    "Pen Testing": "Open"
                }
                comp_cols = st.columns(len(compliance_data_3))
                for idx, (control, status) in enumerate(compliance_data_3.items()):
                    comp_cols[idx].markdown(f"""
                    <div style='background-color:{status_color(status)}; padding:10px; border-radius:8px; text-align:center; color:black; font-weight:bold;'>
                    {control}<br>{status}
                    </div>
                    """, unsafe_allow_html=True)
        
                st.markdown("#### 📝 Notes")
                st.warning("Multiple legacy ports exposed. Rapid remediation in progress.")
