from datetime import date
from pathlib import Path
import sys
import pandas as pd
import streamlit as st
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from src.stock_intelligence import load_stock,summarize,review_rows
st.set_page_config(page_title='Pharma Stock Intelligence',page_icon='💊',layout='wide')
st.title('Pharma Stock Intelligence')
st.caption('Educational MVP • Synthetic data only • Human review required')
with st.sidebar:
    st.header('Analysis settings')
    as_of=st.date_input('Analysis date',value=date.today())
try:
    rows=load_stock(HERE/'data'/'synthetic_stock.csv')
    k=summarize(rows,as_of)
    view=pd.DataFrame(review_rows(rows,as_of))
except Exception as exc:
    st.error(f'Dataset validation failed: {exc}')
    st.stop()
a,b,c=st.columns(3)
a.metric('Stock records',k['records']); b.metric('Total units',f"{k['total_units']:,}"); c.metric('Illustrative value',f"{k['illustrative_stock_value']:,.2f}")
d,e,f=st.columns(3)
d.metric('Expired units',k['expired_units']); e.metric('Near expiry ≤90d',k['near_expiry_units_90d']); f.metric('Low-stock batches',k['low_stock_batches'])
st.subheader('Units by category')
st.bar_chart(view.groupby('category')['quantity'].sum())
st.subheader('Records requiring review')
flagged=view[view.review_flags!='NONE']
st.dataframe(flagged,use_container_width=True,hide_index=True)
st.download_button('Download review CSV',flagged.to_csv(index=False).encode('utf-8-sig'),'stock_review_draft.csv','text/csv')
st.info('Flags are administrative prompts for authorized staff; they do not authorize purchasing, substitution, dispensing or clinical action.')
