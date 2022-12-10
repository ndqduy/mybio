import pandas as pd
import streamlit as st
from mysql.connector import connect 
from cau4 import cau4
from cau5 import cau5
from cau3 import cau3
from cau6 import cau6


def main():
    title = st.title("XEM DANH SÁCH ĐIỂM THI")
    subheader = st.subheader("Yêu cầu:")
    text = st.text("""
    Câu 3: Cho phép xem query trong một tab  gồm các field:
    SBD,  Ho, Ten,  Phai, Tuoi, Toan,  Van, AnhVan, DiemUT, DTN, TongDiem, XepLoai

    Trong đó: 
        DTN: Là điểm thấp nhất của 3 môn Toan, Van, AnhVan.
        TongDiem: Toan + Van + AnhVan + DiemUT
        XepLoai: 
        Nếu TongDiem >= 24 và DTN >= 7:	Giỏi
        Nếu TongDiem >= 21 và DTN >= 6:	Khá
        Nếu TongDiem >= 15 và DTN >= 4:	Trung Bình
        Ngược lại: Trượt


    Cau 4: Cho phép xem query trong một tab gồm Học sinh Phổ thông Khá Giỏi và có ít nhất một môn 10, kết quả được sắp tăng dần theo XepLoai, cùng XepLoai sắp giảm dần theo TongDiem với các field:
    SBD, Ho, Ten, Phai, NTNS, Toan, Van, AnhVan, TongDiem, XepLoai, DoiTuongDT

    Cau 5: Cho phép xem query trong một tab gồm Học sinh Trượt với các field:
    SBD, Ho, Ten, Phai, NTNS, Toan, Van, AnhVan, TongDiem, XepLoai, DoiTuongDT
    Kết quả sắp tăng dần theo đối tượng dự thi, cùng đối tượng sắp giảm dần dự thi theo tổng điểm.

    Cau 6: Cho phép xem query trong một tab gồm Danh sách Học Sinh thủ khoa  có tổng điểm cao nhất với các field:
    SBD, Ho, Ten, Phai, NTNS, Toan, Van, AnhVan, TongDiem, XepLoai, DoiTuongDT

    
	""")


    contact_options = ['cau 3','cau 4', 'cau 5', 'cau 6']
    contact_selected = st.selectbox("Chọn câu", options = contact_options)
    if contact_selected == "cau 4":
        cau4()
    elif contact_selected == "cau 5":
        cau5()
    elif contact_selected == "cau 3":
        cau3()
    elif contact_selected == "cau 6":
        cau6()
if __name__ == "__main__":
    main()