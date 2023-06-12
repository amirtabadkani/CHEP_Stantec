import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title='Cairns Hospital Data Analysis', layout='wide')

# chep_en = pd.read_csv('./data/Energy.csv')

chep_en = pd.read_csv(r'C:\Users\atabadkani\Streamlit Apps\CHEP\data\Energy.csv')

CHEP_en = chep_en.drop('img', axis =1)

st.title("Cairns Hospital Parametric Analysis")

with st.container():
    # st.dataframe(CHEP, use_container_width=True)
    chep_pcm = px.parallel_coordinates(CHEP_en, CHEP_en.columns, color="EUI(kWh/m2)",
                                       labels={"ShadeDepth": "ShadeDepth", "ExWall":"ExWall"},
                                       color_continuous_scale=px.colors.diverging.Tealrose,
                                       color_continuous_midpoint=2, height = 650)
    
    chep_pcm.update_layout(coloraxis_showscale=False)
         
    st.plotly_chart(chep_pcm, use_container_width=True)
    
    
    chep_bx_01 = px.box(CHEP_en, CHEP_en["WWR-NS"], CHEP_en["EUI(kWh/m2)"], "WWR-NS", notched = True)
    chep_bx_02 = px.box(CHEP_en, CHEP_en["WWR-EW"], CHEP_en["EUI(kWh/m2)"], "WWR-EW", notched = True)
    chep_bx_03 = px.box(CHEP_en, CHEP_en["ShadeDepth"], CHEP_en["EUI(kWh/m2)"], "ShadeDepth", notched = True)
    chep_bx_04 = px.box(CHEP_en, CHEP_en["SHGC/VLT"], CHEP_en["EUI(kWh/m2)"], "SHGC/VLT", notched = True)
    chep_bx_05 = px.box(CHEP_en, CHEP_en["ExWall"], CHEP_en["EUI(kWh/m2)"], "ExWall", notched = True)
    chep_bx_06 = px.box(CHEP_en, CHEP_en["ShadeOrientation (0:V, 1:H)"], CHEP_en["EUI(kWh/m2)"], "ShadeOrientation (0:V, 1:H)", notched = True)
    
    cols = st.columns(6)
    
    with cols[0]:
        st.plotly_chart(chep_bx_01, use_container_width=True)
    with cols[1]:
        st.plotly_chart(chep_bx_02, use_container_width=True)
    with cols[2]:
        st.plotly_chart(chep_bx_03, use_container_width=True)
    with cols[3]:
        st.plotly_chart(chep_bx_04, use_container_width=True)
    with cols[4]:
        st.plotly_chart(chep_bx_05, use_container_width=True)
    with cols[5]:
        st.plotly_chart(chep_bx_06, use_container_width=True)

    chep_bx_07 = px.box(CHEP_en, CHEP_en["WWR-NS"], CHEP_en["Average DA"], "WWR-NS", notched = True)
    chep_bx_08 = px.box(CHEP_en, CHEP_en["WWR-EW"], CHEP_en["Average DA"], "WWR-EW", notched = True)
    chep_bx_09 = px.box(CHEP_en, CHEP_en["ShadeDepth"], CHEP_en['Average DA'], "ShadeDepth",  notched = True)
    chep_bx_10 = px.box(CHEP_en, CHEP_en["SHGC/VLT"], CHEP_en['Average DA'], "SHGC/VLT",  notched = True)
    chep_bx_11 = px.box(CHEP_en, CHEP_en["ExWall"], CHEP_en['Average DA'], "ExWall", notched = True)
    chep_bx_12 = px.box(CHEP_en, CHEP_en["ShadeOrientation (0:V, 1:H)"], CHEP_en['Average DA'], "ShadeOrientation (0:V, 1:H)",notched = True)
    
    cols = st.columns(6)
    
    with cols[0]:
        st.plotly_chart(chep_bx_07, use_container_width=True)
    with cols[1]:
        st.plotly_chart(chep_bx_08, use_container_width=True)
    with cols[2]:
        st.plotly_chart(chep_bx_09, use_container_width=True)
    with cols[3]:
        st.plotly_chart(chep_bx_10, use_container_width=True)
    with cols[4]:
        st.plotly_chart(chep_bx_11, use_container_width=True)
    with cols[5]:
        st.plotly_chart(chep_bx_12, use_container_width=True)
        

epic = pd.DataFrame(pd.read_excel(r'C:\Users\atabadkani\Streamlit Apps\CHEP\data\EPiC.xlsx'))

       
def get_index(df) -> dict:
        dict_ = {df['Version: EPiC Database 2019'].iloc[i]: i for i in range(0, len(df['Version: EPiC Database 2019']))}
        return dict_

with st.sidebar:
    
    st.title('Please Choose the Material Type:')
    
    concrete = epic[epic['Version: EPiC Database 2019'].str.contains('Concrete|AAC')]
    concrete = concrete[concrete['Functional unit'] !='no.']
    concrete_type = concrete['Version: EPiC Database 2019'].iloc[:]
    
    concrete_selection = st.selectbox('Concrete:', options=concrete_type, key='concrete', index = 2)
    concrete_unit = concrete['Functional unit'].iloc[int(get_index(concrete)[concrete_selection])]
    concrete_em = concrete['Embodied Greenhouse Gas Emissions (kgCO₂e)'].iloc[int(get_index(concrete)[concrete_selection])]
    st.markdown(f'Unit: {concrete_unit} | Emission Factor (kgCO₂e): {concrete_em}')
    
    
    PB = epic[epic['Version: EPiC Database 2019'].str.contains('Plaster|plaster')]
    PB = PB[PB['Functional unit'] !='no.']
    PB_type = PB['Version: EPiC Database 2019'].iloc[:]
    
    PB_selection = st.selectbox('Plaster Board:', options=PB_type, key='PB', index = 1)
    PB_unit = PB['Functional unit'].iloc[int(get_index(PB)[PB_selection])]
    PB_em = PB['Embodied Greenhouse Gas Emissions (kgCO₂e)'].iloc[int(get_index(PB)[PB_selection])]
    st.markdown(f'Unit: {PB_unit} | Emission Factor (kgCO₂e): {PB_em}')

    Glass = epic[epic['Version: EPiC Database 2019'].str.contains('glazing')]
    Glass = Glass[Glass['Functional unit'] !='no.']
    Glass_type = Glass['Version: EPiC Database 2019'].iloc[:]
    
    Glass_selection = st.selectbox('Glass Type:', options=Glass_type, key='Glass', index = 1)
    Glass_unit = Glass['Functional unit'].iloc[int(get_index(Glass)[Glass_selection])]
    Glass_em = Glass['Embodied Greenhouse Gas Emissions (kgCO₂e)'].iloc[int(get_index(Glass)[Glass_selection])]
    st.markdown(f'Unit: {Glass_unit} | Emission Factor (kgCO₂e): {Glass_em}')
    
    insul = epic[epic['Version: EPiC Database 2019'].str.contains('insulation')]
    insul = insul[insul['Functional unit'] !='no.']
    insul_type = insul['Version: EPiC Database 2019'].iloc[:]
    
    insul_selection = st.selectbox('Insulation Type:', options=insul_type, key='insul', index = 1)
    insul_unit = insul['Functional unit'].iloc[int(get_index(insul)[insul_selection])]
    insul_em = insul['Embodied Greenhouse Gas Emissions (kgCO₂e)'].iloc[int(get_index(insul)[insul_selection])]
    st.markdown(f'Unit: {insul_unit} | Emission Factor (kgCO₂e): {insul_em}')
    
    alum = epic[epic['Version: EPiC Database 2019'].str.contains('Aluminium')]
    alum = alum[alum['Functional unit'] !='no.']
    alum_type = alum['Version: EPiC Database 2019'].iloc[:]
    
    alum_selection = st.selectbox('Aluminimum Type:', options=alum_type, key='alum', index = 4)
    alum_unit = alum['Functional unit'].iloc[int(get_index(alum)[alum_selection])]
    alum_em = alum['Embodied Greenhouse Gas Emissions (kgCO₂e)'].iloc[int(get_index(alum)[alum_selection])]
    st.markdown(f'Unit: {alum_unit} | Emission Factor (kgCO₂e): {alum_em}')
    

with st.container():

    chep_co2 = pd.read_csv(r'C:\Users\atabadkani\Streamlit Apps\CHEP\data\CO2.csv')
    
    CHEP_co2 = chep_co2.drop('img', axis =1)
  
    CHEP_co2.columns
    
    WoL = []
    concrete_calc = []
    PB_calc = []
    Glass_calc = []
    alum_calc  = []
    concerte_density = 2300 #########
    PB_density = 700 #########
    Floor_area = 2310.5  ##########
    grid_factor = 0.85 ###########
    num_years = 20 ######
    
    for i in range(0, len(CHEP_co2)):
        if concrete_unit == 'm³':
            concrete_vol = CHEP_co2['Concrete m3'].iloc[i]*concrete_em
            concrete_calc.append(concrete_vol)
        elif concrete_unit == 'kg':
            concrete_ = concrete_em*concerte_density
            concrete_vol = CHEP_co2['Concrete m3'].iloc[i]*concrete_
            concrete_calc.append(concrete_vol)
        if  PB_unit == 'm²':
            if PB_selection == 'Plasterboard - 10 mm':
                PB_1m = 1/0.01
                PB_ = PB_1m*PB_em
                PB_vol = CHEP_co2['PB m3'].iloc[i]*PB_
                PB_calc.append(PB_vol)
            elif PB_selection == 'Plasterboard - 13 mm':
                PB_1m = 1/0.013
                PB_ = PB_1m*PB_em
                PB_vol = CHEP_co2['PB m3'].iloc[i]*PB_
                PB_calc.append(PB_vol)
        elif PB_unit == 'kg':
                PB_ = PB_em*PB_density
                PB_vol = CHEP_co2['PB m3'].iloc[i]*PB_
                PB_calc.append(PB_vol)
        if Glass_unit == 'm²':
            Glass_vol = CHEP_co2['Glass Area m2'].iloc[i]*Glass_em
            Glass_calc.append(Glass_vol)
        if alum_unit == 'm²':
            alum_vol = CHEP_co2['Shades Area m2'].iloc[i]*alum_em
            alum_calc.append(alum_vol)
        
        Total_vol_emission = concrete_calc+PB_calc+Glass_calc+alum_calc
        WoL = ((CHEP_co2['EUI (kWh/m2)'].iloc[i]*Floor_area*grid_factor)+Total_vol_emission)*num_years
        # WoL.append(WoL)
    WoL
    Total_vol_emission
    # CHEP_co2['WoL'] = WoL
        
    # CHEP_co2   
        
    # chep_pcm = px.parallel_coordinates(CHEP_en, CHEP_en.columns, color="EUI(kWh/m2)",
    #                                    labels={"ShadeDepth": "ShadeDepth", "ExWall":"ExWall"},
    #                                    color_continuous_scale=px.colors.diverging.Tealrose,
    #                                    color_continuous_midpoint=2, height = 650)

# with st.container():
#     chep_bx_13 = px.box(CHEP_co2, CHEP_co2["WWR-NS"], CHEP_co2["Total KgCO2e"], "WWR-NS", notched = True)
#     chep_bx_14 = px.box(CHEP_co2, CHEP_co2["WWR-EW"], CHEP_co2["Total KgCO2e"], "WWR-EW", notched = True)
#     chep_bx_15 = px.box(CHEP_co2, CHEP_co2["ShadeDepth"], CHEP_co2['Total KgCO2e'], "ShadeDepth",  notched = True)
#     chep_bx_16 = px.box(CHEP_co2, CHEP_co2["SHGC/VLT"], CHEP_co2['Total KgCO2e'], "SHGC/VLT",notched = True)
#     chep_bx_17 = px.box(CHEP_co2, CHEP_co2["ExWall"], CHEP_co2['Total KgCO2e'], "ExWall", notched = True)
#     chep_bx_18 = px.box(CHEP_co2, CHEP_co2["ShadeOrientation (0:V, 1:H)"], CHEP_co2['Total KgCO2e'], "ShadeOrientation (0:V, 1:H)", notched = True)
        
#     cols = st.columns(6)
    
#     with cols[0]:
#         st.plotly_chart(chep_bx_13, use_container_width=True)
#     with cols[1]:
#         st.plotly_chart(chep_bx_14, use_container_width=True)
#     with cols[2]:
#         st.plotly_chart(chep_bx_15, use_container_width=True)
#     with cols[3]:
#         st.plotly_chart(chep_bx_16, use_container_width=True)
#     with cols[4]:
#         st.plotly_chart(chep_bx_17, use_container_width=True)
#     with cols[5]:
#         st.plotly_chart(chep_bx_18, use_container_width=True)  
        
        
