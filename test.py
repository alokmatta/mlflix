import sys
import shutil
import os
import streamlit as st

st.markdown(
    """
| Col1      | Col2        |
| --------- | ----------- |
| Some      | Data        |
"""
)

total, used, free = shutil.disk_usage("/")

print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))

print(sys.executable)
print(os.environ)
