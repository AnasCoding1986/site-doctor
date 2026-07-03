import streamlit as st
from agent import run_agent

st.set_page_config(
    page_title="Site Doctor",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Site Doctor")
st.markdown("### AI-Powered Web Accessibility & SEO Audit")

st.markdown("---")

st.markdown("#### Enter Website URL:")
url = st.text_input(
    "Website URL",
    placeholder="https://example.com",
    label_visibility="collapsed"
)

if st.button("🔍 Analyze Website", use_container_width=True):
    if not url:
        st.error("⚠️ Please enter a website URL")
    else:
        with st.spinner("🔄 Analyzing website... This may take a moment..."):
            try:
                result = run_agent(url)

                st.markdown("---")
                st.markdown("### 📊 Audit Results")

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Issues Found", result['evaluation']['total_issues'])
                    st.metric("Score Before", f"{result['evaluation']['score_before']}/100")

                with col2:
                    st.metric("Issues Fixed", result['evaluation']['issues_fixed'])
                    st.metric("Score After", f"{result['evaluation']['score_after']}/100")

                improvement = result['evaluation']['compliance_percentage']
                st.success(f"✓ Compliance improved by {improvement:.1f}% after fixes")

                st.markdown("---")
                st.markdown("### 📄 Full Report")
                st.markdown(result['report'])

                safe_name = url.replace('https://', '').replace('http://', '').replace('/', '_')

                st.download_button(
                    label="📥 Download Report as PDF",
                    data=result['pdf_bytes'],
                    file_name=f"site_doctor_report_{safe_name}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")