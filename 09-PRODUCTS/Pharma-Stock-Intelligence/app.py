from datetime import date
from pathlib import Path
import sys
import pandas as pd
import streamlit as st
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from src.stock_intelligence import load_stock,summarize,review_rows
from src.advanced_analytics import read_csv,consumption_summary,abc_analysis,fefo_review,fsn_classification
st.set_page_config(page_title="Pharma Stock Intelligence",page_icon="💊",layout="wide")
st.title("Pharma Stock Intelligence")
st.caption("Pharmacy operations analytics • Synthetic training data • Human review required")
with st.sidebar:
 st.header("Analysis parameters")
 as_of=st.date_input("Analysis date",value=date(2026,11,19))
 lookback=st.slider("Consumption lookback (days)",30,180,120,15)
 lead=st.slider("Assumed supplier lead time (days)",0,90,21)
 safety=st.slider("Safety buffer (days)",0,60,14)
 target=st.slider("Target stock horizon (days)",15,120,45,5)
try:
 stock=load_stock(HERE/"data"/"synthetic_stock.csv")
 usage=read_csv(HERE/"data"/"synthetic_consumption.csv")
 k=summarize(stock,as_of)
 stock_view=pd.DataFrame(review_rows(stock,as_of))
 replenishment=pd.DataFrame(consumption_summary(stock,usage,as_of,lookback,lead,safety,target))
 abc=pd.DataFrame(abc_analysis(stock,usage,as_of,lookback))
 fefo=pd.DataFrame(fefo_review(stock,as_of,120))
 fsn=pd.DataFrame(fsn_classification(usage,as_of,[r["product_id"] for r in stock]))
except Exception as exc:
 st.error(f"Data validation failed: {exc}"); st.stop()
st.warning("Training prototype only. Planning parameters are assumptions, not procurement instructions. Verify stock, units, lead times and local SOP before any action.")
t1,t2,t3,t4=st.tabs(["Inventory overview","Consumption & replenishment","ABC / FSN analysis","Expiry & FEFO"])
with t1:
 a,b,c=st.columns(3); a.metric("Records",k["records"]); b.metric("Units on hand",f'{k["total_units"]:,}'); c.metric("Illustrative stock value",f'{k["illustrative_stock_value"]:,.2f}')
 d,e,f=st.columns(3); d.metric("Expired units",k["expired_units"]); e.metric("Near expiry ≤90d",k["near_expiry_units_90d"]); f.metric("Below static reorder level",k["low_stock_batches"])
 st.subheader("Units by category"); st.bar_chart(stock_view.groupby("category")["quantity"].sum())
 st.subheader("Batch review queue"); flagged=stock_view[stock_view.review_flags!="NONE"]; st.dataframe(flagged,use_container_width=True,hide_index=True)
 st.download_button("Export batch review CSV",flagged.to_csv(index=False).encode("utf-8-sig"),"batch_review.csv","text/csv")
with t2:
 st.subheader("Consumption-based planning")
 st.caption("Average daily issues = units issued in lookback ÷ days. Reorder point = average daily issues × (lead time + safety days). Suggested quantity targets the selected horizon plus safety stock.")
 st.dataframe(replenishment,use_container_width=True,hide_index=True)
 st.download_button("Export replenishment review CSV",replenishment.to_csv(index=False).encode("utf-8-sig"),"replenishment_review.csv","text/csv")
 st.info("Observed issues may understate demand during stockouts. Supplier variability, seasonality, returns, transfers, pack conversion and minimum order quantities are not modeled.")
with t3:
 st.subheader("ABC by usage value"); st.caption("ABC ranks issued quantity × illustrative unit cost. It is not clinical criticality.")
 st.dataframe(abc,use_container_width=True,hide_index=True)
 st.subheader("FSN movement"); st.caption("F = issue in last 30 days; S = last issue 31–90 days ago; N = no issue or last issue >90 days ago.")
 st.dataframe(fsn,use_container_width=True,hide_index=True)
with t4:
 st.subheader("FEFO / expiry review"); st.caption("Earliest expiry first. Expired stock is a quarantine/disposition review prompt under local policy.")
 st.dataframe(pd.DataFrame(fefo),use_container_width=True,hide_index=True)
 st.download_button("Export expiry review CSV",pd.DataFrame(fefo).to_csv(index=False).encode("utf-8-sig"),"fefo_review.csv","text/csv")
st.caption("All supplied inventory and issue records are synthetic. Outputs are administrative prompts, never automatic orders, dispensing or treatment decisions.")
