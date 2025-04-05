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
def simulate_shieldinsights_trigger(use_case):
    if use_case == "M&A Integration Support":
        return ["SecureEdge", "MergiTrust", "DataDefend"]
    elif use_case == "IAM Remediation":
        return ["CloudSentinel", "TrustWare"]
    elif use_case == "Cloud Security Hardening":
        return ["SkyFence", "NetArmor"]
    else:
        return ["TrustWare", "SecureEdge"]

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
    st.dataframe(vendor_df)

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
