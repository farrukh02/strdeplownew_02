###############################
# This program lets you       #
# - enter values in Streamlit #
# - get prediction            #  
###############################
import pickle
#######from turtle import st

import pandas as pd
import streamlit as st

# loading the model
 #path = ''
modelname = 'toymodel_02.pkl'
loaded_model = pickle.load(open(modelname, 'rb'))
#2#
modelname_02 = 'catboost_3222_f02.pickle'
loaded_model_02 = pickle.load(open(modelname_02, 'rb'))
#############
# Main page #
#############                
st.write("The model prediction")

# LIVINGAPARTMENTS_AVG_MIN = 0.0
# LIVINGAPARTMENTS_AVG_MAX = 1.0
# APARTMENTS_AVG_MIN = 0.0
# APARTMENTS_AVG_MAX = 0.11697126743049956

# Get input values - numeric variables
# LIVINGAPARTMENTS_AVG = st.slider('Please enter the living apartments:',
#                                 min_value=LIVINGAPARTMENTS_AVG_MIN,
#                                 max_value=LIVINGAPARTMENTS_AVG_MAX
#                                 )
# APARTMENTS_AVG = st.slider('Please enter the apartment average:',
#                           min_value=APARTMENTS_AVG_MIN,
#                         max_value=APARTMENTS_AVG_MAX
#                           )

# Set dummy variables to zero    
cat_list = ['ord_T_q_9101a_3', 'ord_T_q_9101a_4', 'ord_T_q_9101a_5',
            'ord_T_q_9101a_7', 'ord_T_q_9101a_8', 'ord_T_q_9101b_1',
            'ord_T_q_9101b_2', 'ord_T_q_9101b_3', 'ord_T_q_9101b_4',
            'ord_T_q_9101b_6', 'ord_T_q_9101b_7', 'ord_T_q_9101c_1',
            'ord_T_q_9101c_2', 'ord_T_q_9101c_4', 'ord_T_q_9101c_6',
            'ord_T_q_9101c_7', 'ord_T_q_9101c_8', 'ord_T_q_9101c_9',
            'ord_T_q_9101d_2', 'ord_T_q_9101d_3', 'ord_T_q_9101d_4',
            'ord_T_q_9101d_6', 'ord_T_q_9101d_7', 'ord_T_q_9101d_8',
            'ord_T_q_9101d_9', 'ord_T_q_9101e_1', 'ord_T_q_9101e_2',
            'ord_T_q_9101e_4', 'ord_T_q_9101e_7', 'ord_T_q_9101e_8',
            'ord_T_q_9101f_2', 'nom_q_1102_Man', 'nom_q_1102_Women',
            'nom_q_1111_Dushanbe', 'nom_q_1111_GBAO', 'nom_q_1111_Khatlon', 'nom_q_1111_Sogd', 'nom_q_1111_Subordination_center'
            'nom_q_1110_City', 'nom_q_1110_Village',  'nom_q_9103b', 'nom_q_9103c', 'nom_q_9103d', 'nom_q_9103e',
            'nom_q_9103f', 'nom_q_9103g', 'nom_q_9103h', 'nom_q_9103i',
            'nom_q_9103j', 'nom_q_9103k', 'nom_q_9103l', 'nom_q_9103m',
            'nom_q_9103n', 'nom_q_9103o', 'nom_q_9103p', 'nom_q_9103q',
            'nom_q_9103r', 'nom_q_9103s', 'nom_q_9204']
for i in cat_list:
    exec("%s = %d" % (i, 0))  # The exec() command makes a value as the variable name

# Enter data for prediction
ord_T_q_9101a_3 = st.selectbox('(ord_T_q_9101a_3)',
                           ('1',
                            '2',
                            '0',
                            '4',
                            '3')
                           )
ord_T_q_9101a_4 = st.selectbox('(ord_T_q_9101a_4)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )
ord_T_q_9101a_5 = st.selectbox('(ord_T_q_9101a_5)',
                           ('1',
                            '2',
                            '0',
                            '4',
                            '3')
                           )
ord_T_q_9101a_7 = st.selectbox('(ord_T_q_9101a_7)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )
ord_T_q_9101a_8 = st.selectbox('(ord_T_q_9101a_8)',
                           ('1',
                            '2',
                            '0',
                            '4',
                            '3')
                           )
ord_T_q_9101b_1 = st.selectbox('(ord_T_q_9101b_1)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )
ord_T_q_9101b_2 = st.selectbox('(ord_T_q_9101b_2)',
                           ('1',
                            '2',
                            '0',
                            '4',
                            '3')
                           )
ord_T_q_9101b_3 = st.selectbox('(ord_T_q_9101b_3)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )
ord_T_q_9101b_4 = st.selectbox('(ord_T_q_9101b_4)',
                           ('1',
                            '2',
                            '0',
                            '4',
                            '3')
                           )
ord_T_q_9101b_6 = st.selectbox('(ord_T_q_9101b_6)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )
ord_T_q_9101b_7 = st.selectbox('(ord_T_q_9101b_7)',
                           ('1',
                            '2',
                            '0',
                            '4',
                            '3')
                           )
ord_T_q_9101c_1 = st.selectbox('(ord_T_q_9101c_1)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )
ord_T_q_9101c_2 = st.selectbox('(ord_T_q_9101c_2)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )
ord_T_q_9101c_4 = st.selectbox('(ord_T_q_9101c_4)',
                           ('1',
                            '2',
                            '0',
                            '4',
                            '3')
                           )
ord_T_q_9101c_6 = st.selectbox('(ord_T_q_9101c_6)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )
ord_T_q_9101c_7 = st.selectbox('(ord_T_q_9101c_7)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )

ord_T_q_9101c_8 = st.selectbox('(ord_T_q_9101c_8)',
                           ('1',
                            '2',
                            '0',
                            '4',
                            '3')
                           )
ord_T_q_9101c_9 = st.selectbox('(ord_T_q_9101c_9)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )
ord_T_q_9101d_2 = st.selectbox('(ord_T_q_9101d_2)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )
ord_T_q_9101d_3 = st.selectbox('(ord_T_q_9101d_3)',
                           ('1',
                            '2',
                            '0',
                            '4',
                            '3')
                           )
ord_T_q_9101d_4 = st.selectbox('(ord_T_q_9101d_4)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )
ord_T_q_9101d_6 = st.selectbox('(ord_T_q_9101d_6)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )
ord_T_q_9101d_7 = st.selectbox('(ord_T_q_9101d_7)',
                           ('1',
                            '2',
                            '0',
                            '4',
                            '3')
                           )
ord_T_q_9101d_8 = st.selectbox('(ord_T_q_9101d_8)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )
ord_T_q_9101d_9 = st.selectbox('(ord_T_q_9101d_9)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )
ord_T_q_9101e_1 = st.selectbox('(ord_T_q_9101e_1)',
                           ('1',
                            '2',
                            '0',
                            '4',
                            '3')
                           )
ord_T_q_9101e_2 = st.selectbox('(ord_T_q_9101e_2)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )

ord_T_q_9101e_4 = st.selectbox('(ord_T_q_9101e_4)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )
ord_T_q_9101e_7 = st.selectbox('(ord_T_q_9101e_7)',
                           ('1',
                            '2',
                            '0',
                            '4',
                            '3')
                           )
ord_T_q_9101e_8 = st.selectbox('(ord_T_q_9101e_8)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3')
                               )

ord_T_q_9101f_2 = st.selectbox('(ord_T_q_9101f_2)',
                                ('1',
                                 '2',
                                 '0',
                                 '4',
                                 '3',
                                 '5')
                               )

nom_q_1102_Man = st.selectbox('(nom_q_1102_Man)',
                               ('1',
                                '0')
                               )
nom_q_1102_Women = st.selectbox('(nom_q_1102_Women)',
                           ('1',
                            '0')
                            )
nom_q_1111_Dushanbe = st.selectbox('(nom_q_1111_Dushanbe)',
                               ('1',
                                '0')
                               )
nom_q_1111_GBAO = st.selectbox('(nom_q_1111_GBAO)',
                           ('1',
                            '0')
                            )
nom_q_1111_Khatlon = st.selectbox('(nom_q_1111_Khatlon)',
                               ('1',
                                '0')
                               )
nom_q_1111_Sogd = st.selectbox('(nom_q_1111_Sogd)',
                           ('1',
                            '0')
                            )
#####
nom_q_1111_Subordination_center = st.selectbox('(nom_q_1111_Subordination_center)',
                                ('1',
                                 '0')
                               )
#####
nom_q_1110_City = st.selectbox('(nom_q_1110_City)',
                           ('1',
                            '0')
                            )
nom_q_1110_Village = st.selectbox('(nom_q_1110_Village)',
                               ('1',
                                '0')
                               )


##model 2###
nom_q_9103b = st.selectbox('(nom_q_9103_b)',
                           ('Electronics',
                            'Chemistry')
                           )
nom_q_9103c = st.selectbox('(nom_q_9103_c)',
                           ('Photography',
                            'Botany')
                           )
nom_q_9103d = st.selectbox('(nom_q_9103d)',
                           ('Owning a store',
                            'Advice on work')
                           )
nom_q_9103e = st.selectbox('(nom_q_9103e)',
                           ('Company management',
                            'Helping families in need')
                           )
nom_q_9103f = st.selectbox('(nom_q_9103f)',
                           ('Physical training',
                            'Doktor')
                           )
nom_q_9103g = st.selectbox('(nom_q_9103g)',
                           ('Music',
                            'Working with wood')
                           )
nom_q_9103h = st.selectbox('(nom_q_9103h)',
                           ('Physics',
                            'Economic sciences')
                           )
nom_q_9103i = st.selectbox('(nom_q_9103i)',
                           ('Education',
                            'Art')
                           )
nom_q_9103j = st.selectbox('(nom_q_9103j)',
                           ('Law',
                            'Artist / Folk Crafts')
                           )
nom_q_9103k = st.selectbox('(nom_q_9103k)',
                           ('Child care',
                            'Stand electronics')
                           )

nom_q_9103l = st.selectbox('(nom_q_9103l)',
                           ('Landscaping',
                            'Playing in a group, being a member of a music team')
                           )
nom_q_9103m = st.selectbox('(nom_q_9103m)',
                           ('Travel agent',
                            'Mechanic')
                           )
nom_q_9103n = st.selectbox('(nom_q_9103n)',
                           ('Work in the office',
                            'Picture description')
                           )
nom_q_9103o = st.selectbox('(nom_q_9103o)',
                           ('Forest',
                            'The nurse of mercy')
                           )
nom_q_9103p = st.selectbox('(nom_q_9103p)',
                           ('Electric', 'Economist'))

nom_q_9103q = st.selectbox('(nom_q_9103q)',
                           ('Accounting', 'Geology'))

nom_q_9103r = st.selectbox('(nom_q_9103r)',
                           ('Builder', 'Economist'))

nom_q_9103s = st.selectbox('(nom_q_9103s)',
                           ('Confirmation of a home loan (mortgage)',
                            'Helping patients in the hospital')
                           )

#'1',
  #                          '2',
   #                         '0',
    #                        '4',
     #                       '3'
#if ord_T_q_9101a_3 == '1':
 #   1 = 1
#elif ord_T_q_9101a_3 == '2':
#    2 = 1
#elif ord_T_q_9101a_3 == '0':
#    0 = 1
#elif ord_T_q_9101a_3 == '4':
#    4 = 1
#elif ord_T_q_9101a_3 == '4':
#    4 = 1

##2 model###
if nom_q_9103b == 'Electronics':
    Electronics = 1
elif nom_q_9103b == 'Chemistry':
    Chemistry = 1

elif nom_q_9103c == 'Botany':
    Botany = 1
elif nom_q_9103c == 'Photography':
    Photography = 1

elif nom_q_9103d == 'Owning_store':
    Owning_store = 1
elif nom_q_9103d == 'Advice_on_work':
    Advice_on_work = 1

elif nom_q_9103e == 'Company_management':
    Company_management = 1
elif nom_q_9103e == 'Helping_families_in_need':
    Helping_families_in_need = 1

elif nom_q_9103f == 'Physical_training':
    Physical_training = 1
elif nom_q_9103f == 'Doktor':
    Doktor = 1

elif nom_q_9103g == 'Music':
    Music = 1
elif nom_q_9103g == 'Working_with_wood':
    Working_with_wood = 1

elif nom_q_9103h == 'Physics':
    Physics = 1
elif nom_q_9103h == 'Economic_sciences':
    Economic_sciences = 1

elif nom_q_9103i == 'Education':
    Education = 1
elif nom_q_9103i == 'Art':
    Art = 1

if nom_q_9103j == 'Law':
    Law = 1
elif nom_q_9103j == 'Artist_Folk_Crafts':
    Artist_Folk_Crafts = 1

elif nom_q_9103k == 'Child_care':
    Child_care = 1
elif nom_q_9103k == 'Stand_electronics':
    Stand_electronics = 1


elif nom_q_9103l == 'Landscaping':
    Landscaping = 1
elif nom_q_9103l == 'Playing_in_group':
    Playing_in_group = 1

elif nom_q_9103m == 'Travel_agent':
    Travel_agent = 1
elif nom_q_9103m == 'Mechanic':
    Mechanic = 1

elif nom_q_9103n == 'Work_office':
    Work_office = 1
elif nom_q_9103n == 'Picture_description':
    Picture_description = 1

elif nom_q_9103o == 'nurse_mercy':
    nurse_mercy = 1
elif nom_q_9103o == 'Forest':
    Forest = 1

elif nom_q_9103p == 'Economist':
    Economist = 1
elif nom_q_9103p == 'Electric':
    Electric = 1

elif nom_q_9103q == 'Accounting':
    Accounting = 1
elif nom_q_9103q == 'Geology':
    Geology = 1

elif nom_q_9103r == 'Economist':
    Economist = 1
elif nom_q_9103r == 'Builder':
    Builder = 1

elif nom_q_9103s == 'helping_hospital':
    helping_hospital = 1
elif nom_q_9103s == 'mortgage':
    mortgage = 1

#elif nom_q_9204 == 'OTHER':
 #   OTHER = 1
# when 'Predict' is clicked, make the prediction and store it
if st.button("Get Your Prediction career"):
    Xp = pd.DataFrame({'ord_T_q_9101a_3': [ord_T_q_9101a_3],
                          'ord_T_q_9101a_4': [ord_T_q_9101a_4],
                          'ord_T_q_9101a_5': [ord_T_q_9101a_5],
                          'ord_T_q_9101a_7': [ord_T_q_9101a_7],
                          'ord_T_q_9101a_8': [ord_T_q_9101a_8],
                          'ord_T_q_9101b_1': [ord_T_q_9101b_1],
                          'ord_T_q_9101b_2': [ord_T_q_9101b_2],
                          'ord_T_q_9101b_3': [ord_T_q_9101b_3],
                          'ord_T_q_9101b_4': [ord_T_q_9101b_4],
                          'ord_T_q_9101b_6': [ord_T_q_9101b_6],
                          'ord_T_q_9101b_7': [ord_T_q_9101b_7],
                          'ord_T_q_9101c_1': [ord_T_q_9101c_1],
                          'ord_T_q_9101c_2': [ord_T_q_9101c_2],
                          'ord_T_q_9101c_4': [ord_T_q_9101c_4],
                          'ord_T_q_9101c_6': [ord_T_q_9101c_6],
                          'ord_T_q_9101c_7': [ord_T_q_9101c_7],
                          'ord_T_q_9101c_8': [ord_T_q_9101c_8],
                          'ord_T_q_9101c_9': [ord_T_q_9101c_9],
                          'ord_T_q_9101d_2': [ord_T_q_9101d_2],
                          'ord_T_q_9101d_3': [ord_T_q_9101d_3],
                          'ord_T_q_9101d_4': [ord_T_q_9101d_4],
                          'ord_T_q_9101d_6': [ord_T_q_9101d_6],
                          'ord_T_q_9101d_7': [ord_T_q_9101d_7],
                          'ord_T_q_9101d_8': [ord_T_q_9101d_8],
                          'ord_T_q_9101d_9': [ord_T_q_9101d_9],
                          'ord_T_q_9101e_1': [ord_T_q_9101e_1],
                          'ord_T_q_9101e_2': [ord_T_q_9101e_2],
                          'ord_T_q_9101e_4': [ord_T_q_9101e_4],
                          'ord_T_q_9101e_7': [ord_T_q_9101e_7],
                          'ord_T_q_9101e_8': [ord_T_q_9101e_8],
                          'ord_T_q_9101f_2': [ord_T_q_9101f_2],
                          'nom_q_1102_Man': [nom_q_1102_Man],
                          'nom_q_1102_Women': [nom_q_1102_Women],
                          'nom_q_1111_Dushanbe': [nom_q_1111_Dushanbe],
                          'nom_q_1111_GBAO': [nom_q_1111_GBAO],
                          'nom_q_1111_Khatlon': [nom_q_1111_Khatlon],
                          'nom_q_1111_Sogd': [nom_q_1111_Sogd],
                          'nom_q_1111_Subordination_center': [nom_q_1111_Subordination_center],
                          'nom_q_1110_City': [nom_q_1110_City],
                          'nom_q_1110_Village': [nom_q_1110_Village],
                          })
    # Making predictions
    #prediction = loaded_model.predict(X)[:, 1]  # The model produces (p0,p1), we want p1.
    #predictions = loaded_model.predict(X)
    def predictions(Xp):
        import operator
        res_02 = loaded_model_02.predict_proba(Xp).flatten().tolist()
        res_02 = [i*100 for i in res_02]
        prof = ["business","creative","office","outdoors","people_contact","practical","scientific"]
        d = dict(zip(prof,res_02))
        sorted_dict = sorted(d.items(),key = operator.itemgetter(1),reverse=True)
        return sorted_dict
    predictions_03 = predictions(Xp)

    st.success('Your Target is {}'.format(predictions_03))
##2model#
if st.button("Get Your Prediction"):
    X = pd.DataFrame({'nom_q_9103b': [nom_q_9103b],
                          'nom_q_9103c': [nom_q_9103c],
                          'nom_q_9103d': [nom_q_9103d],
                          'nom_q_9103e': [nom_q_9103e],
                          'nom_q_9103f': [nom_q_9103f],
                          'nom_q_9103g': [nom_q_9103g],
                          'nom_q_9103h': [nom_q_9103h],
                          'nom_q_9103i': [nom_q_9103i],
                          'nom_q_9103j': [nom_q_9103j],
                          'nom_q_9103k': [nom_q_9103k],
                          'nom_q_9103l': [nom_q_9103l],
                          'nom_q_9103m': [nom_q_9103m],
                          'nom_q_9103n': [nom_q_9103n],
                          'nom_q_9103o': [nom_q_9103o],
                          'nom_q_9103p': [nom_q_9103p],
                          'nom_q_9103q': [nom_q_9103q],
                          'nom_q_9103r': [nom_q_9103r],
                          'nom_q_9103s': [nom_q_9103s],
                          })
    # Making predictions            
    #prediction = loaded_model.predict(X)[:, 1]  # The model produces (p0,p1), we want p1.
    #predictions = loaded_model.predict(X)
    def predictions(X):
        import operator
        res = loaded_model.predict_proba(X).flatten().tolist()
        res = [i*100 for i in res]
        prof = ["business","creative","office","outdoors","people_contact","practical","scientific"]
        d = dict(zip(prof,res))
        sorted_dict = sorted(d.items(),key = operator.itemgetter(1),reverse=True)
        return sorted_dict
    predictions_02 = predictions(X)

    st.success('Your Target is {}'.format(predictions_02))
