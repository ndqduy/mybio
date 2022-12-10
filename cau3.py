import pandas as pd
import streamlit as st
from mysql.connector import connect 
query_cau_3 = ("select SBD, Ho, Ten, Phai, (YEAR(CURDATE()) - YEAR(ngay_sinh)) AS Tuoi, Toan, Van, anh_van, diem_ut, DTN, tong_diem, "
                            +"IF(tong_diem >= 24 AND DTN >= 7,'Gioi', "
                            +"IF(tong_diem >= 21 AND DTN >= 6, 'Kha', "
                            +"IF(tong_diem >= 15 AND DTN >= 4, 'Trung binh', 'Chua Dat')))"
                            +"As Xep_Loai from tmp_diem_thi_tong_hop order by SBD;")
def cau3():
    def connect_database_table():
        # Bước 1: Connect database db_quan_ly_diem_thi
        try:
            connect_database = connect(
                host="localhost",
                user="root",
                password="QuocDuy2003",
                database="db_quan_ly_diem_thi"
            )
        except:
            print('Không thể kết nối với database')
            exit()

        database_cursor = connect_database.cursor()
        # Bước 2: Xem table tbl_diem_thi_tong_hop
        query_xem_table = query_cau_3
        try:
            database_cursor.execute(query_xem_table)
        except:
            print('Không thể thực hiện query')
            exit()
                
        result = database_cursor.fetchall()
        return result
        # Lấy dữ liệu xong
        # Đóng cursor
        database_cursor.close()
        # Đóng database
        connect_database.close()

    result = connect_database_table()
    lst_SBD = []
    lst_Ho = []
    lst_Ten = []
    lst_phai = []
    lst_tuoi = []
    lst_toan = []
    lst_van = []
    lst_anhvan = []
    lst_diemut = []
    lst_dtn = []
    lst_tongdiem = []
    lst_xeploai = []
    for row in result:
        SBD =        row[0]
        ho =         row[1]
        ten =        row[2]
        phai =       row[3]
        tuoi =       row[4]
        toan =       row[5]
        van =        row[6]
        anh_van =    row[7]
        diem_ut=     row[8]
        dtn =        row[9]
        tong_diem =  row[10]
        xep_loai =   row[11]
        # Chuyển số và ngày thành chuỗi
        f_toan = '%.1f' %toan 
        f_van = '%.1f' %van 
        f_anhvan = '%.1f' %anh_van 
        f_tongdiem = '%.1f' %tong_diem 
        s_SBD = '%3d' %SBD
        s_Phai = '%1d' %phai
        # Append elememt to list 
        lst_SBD.append(s_SBD)
        lst_Ho.append(ho)
        lst_Ten.append(ten)
        lst_phai.append(s_Phai)
        lst_tuoi.append(tuoi)
        lst_toan.append(f_toan)
        lst_van.append(f_van)
        lst_anhvan.append(f_anhvan)
        lst_diemut.append(diem_ut)
        lst_dtn.append(dtn)
        lst_tongdiem.append(f_tongdiem)
        lst_xeploai.append(xep_loai)
                    
    # Cache the dataframe so it's only loaded once
    @st.experimental_memo
    def load_data():
        return pd.DataFrame(
            {
                "SBD": lst_SBD,
                "Họ": lst_Ho,
                "Tên": lst_Ten,
                "Phái": lst_phai,
                "Tuổi": lst_tuoi,
                "Toán": lst_toan,
                "Văn": lst_van,
                "Anh Văn": lst_anhvan,
                "Điểm ưu tiên": lst_diemut,
                "Điểm thấp nhất": lst_dtn,
                "Tổng Điểm": lst_tongdiem,
                "Xếp loại": lst_xeploai,
            }
        )
    # Boolean to resize the dataframe, stored as a session state variable
    st.checkbox("Use container width", value=False, key="use_container_width")


    # Display the dataframe and allow the user to stretch the dataframe
    # across the full width of the container, based on the checkbox value
    df = load_data()
    st.dataframe(df, use_container_width=st.session_state.use_container_width)

def main():
    cau3()
if __name__ == "__main__":
    main()