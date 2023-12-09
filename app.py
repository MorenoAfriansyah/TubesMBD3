import streamlit as st
from sqlalchemy import text

list_dosen = ['', 'Dra. Sri Mumpuni Retnaningsih, M.T', 'Dra. Lucia Aridinanti, M.Si', 'Dr. Wahyu Wibowo, S.Si, M.Si', 'Iis Dewi Ratih, S.Si, M.Si', 'Ir. Sri Pingit Wulandari, M.Si']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://morenoafriansyah10:f7XqjhuW3VwA@ep-solitary-pine-44076365-pooler.ap-southeast-1.aws.neon.tech/tubesmbd3")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS SCHEDULE (id serial, nama_dosen varchar, nip varchar, departemen_dosen varchar, pendidikan_dosen varchar, \
                                                       sosmed text);')
    session.execute(query)

st.header('ITS LECTURER DATABASE SYSTEM')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM schedule ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO schedule (nama_dosen, nip, departemen_dosen, pendidikan_dosen, sosmed) \
                          VALUES (:1, :2, :3, :4, :5);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'', '5':''})
            session.commit()

    data = conn.query('SELECT * FROM schedule ORDER By id;', ttl="0")
    for _, result in data.iterrows():        
        id = result['id']
        nama_dosen_lama = result["nama_dosen"]
        nip_lama = result["nip"]
        departemen_dosen_lama = result["departemen_dosen"]
        pendidikan_dosen_lama = result["pendidikan_dosen"]
        sosmed_lama = result["sosmed"]

        with st.expander(f'a.n. {departemen_dosen_lama}'):
            with st.form(f'data-{id}'):
                nama_dosen_baru = st.text_input("nama_dosen", nama_dosen_lama)
                nip_baru = st.text_input("nip", nip_lama)
                departemen_dosen_baru = st.text_input("departemen_dosen", departemen_dosen_lama)
                pendidikan_dosen_baru = st.text_input("pendidikan_dosen", pendidikan_dosen_lama)
                sosmed_baru = st.text_input("sosmed", sosmed_lama)

                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE schedule \
                                          SET nama_dosen=:1, nip=:2, departemen_dosen=:3, pendidikan_dosen=:4, sosmed=:5, \
                                          WHERE id=:6;')
                            session.execute(query, {'1':nama_dosen_baru, '2':nip_baru, '3':departemen_dosen_baru, '4':pendidikan_dosen_baru, '5':sosmed_baru, '6':id})
                            session.commit()
                            st.experimental_rerun()

                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM schedule WHERE id=:1;')
                        session.execute(query, {'1':id})
                        session.commit()
                        st.experimental_rerun()
