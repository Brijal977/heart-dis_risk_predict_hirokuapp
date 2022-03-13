import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


def load_data():
    data = pd.read_csv('data/heart_Disease_PKI.csv')
    return data


def preprocess_df():
    processed_data = load_data()
    le = LabelEncoder()

    processed_data['Sex'] = le.fit_transform(processed_data['Sex'])
    processed_data['Race'] = le.fit_transform(processed_data['Race'])
    processed_data['Smoking'] = le.fit_transform(processed_data['Smoking'])
    processed_data['AgeCategory'] = le.fit_transform(processed_data['AgeCategory'])
    processed_data['DiffWalking'] = le.fit_transform(processed_data['DiffWalking'])
    processed_data['PhysicalActivity'] = le.fit_transform(processed_data['PhysicalActivity'])
    processed_data['GenHealth'] = le.fit_transform(processed_data['GenHealth'])
    processed_data['HeartDisease'] = le.fit_transform(processed_data['HeartDisease'])
    processed_data['Stroke'] = le.fit_transform(processed_data['Stroke'])
    processed_data['Diabetic'] = le.fit_transform(processed_data['Diabetic'])
    processed_data['Asthma'] = le.fit_transform(processed_data['Asthma'])
    processed_data['SkinCancer'] = le.fit_transform(processed_data['SkinCancer'])
    processed_data['PhysicalActivity'] = le.fit_transform(processed_data['PhysicalActivity'])
    processed_data['AlcoholDrinking'] = le.fit_transform(processed_data['AlcoholDrinking'])
    processed_data['KidneyDisease'] = le.fit_transform(processed_data['KidneyDisease'])

    return processed_data


heart = load_data()
df = preprocess_df()


def show_explore_page():
    st.title("Explore the heart disease facts")

    st.write(""" 
    ### Numerical feathers : Division of heart patients based on specific patient feathers """)

    # sns.set(rc={'axes.backcolor': '#CBEAED', 'figure.backcolor': '#CBEAED'})
    fig1, ax = plt.subplots(3, 3, figsize=(30, 20))

    for i, feature in enumerate(
            ['Sex', 'Stroke', 'Smoking', 'PhysicalActivity', 'Asthma', 'AgeCategory', 'KidneyDisease', 'GenHealth',
             'SkinCancer']):
        colors = ['#51AF5B', '#FF6600', '#161616', '#019267', '#EFDAD7', '#C84B31', '#F0A500', '#D82148', '#151D3B',
                  '#5463FF', '#06FF00', '#461111', '#AA14F0', '#FF8303', '#DA1212']

        sns.countplot(x=feature, data=heart, ax=ax[i // 3, i % 3], palette=colors, alpha=0.8, edgecolor='black',
                      linewidth=2)
        ax[i // 3, i % 3].grid(b=True, which='major', color='black', linewidth=0.2)
        ax[i // 3, i % 3].set_title('Based on {}'.format(feature), color='black', fontsize=18)
        ax[i // 3, i % 3].set_ylabel('number of patients', color='black', fontsize=12)
        ax[i // 3, i % 3].set_xlabel('Heart patients', color='black', fontsize=12)

    plt.tight_layout(pad=10.0)
    st.pyplot(fig1)
    # plt.show()

    st.write(""" ### Correlation Matrix (pearson correlation """)

    st.write("""Visualizing the data features to find the 
    correlation between them which will infer the important features""")
    fig2 = plt.figure(figsize=(20, 12))
    fig2.patch.set_facecolor('white')
    sns.heatmap(df.corr(method='pearson', min_periods=1), annot=True)

    st.pyplot(fig2)

    st.write(""" 
     ### Proportional feathers : Division of heart patients based on specific patient feathers """)
    st.write("Distribution on dataset based on feathers")

    def draw_semi_pie_chart(data, column, fig, renamed_index_dict, title):
        default_colors = ['#008E89', '#85F4FF']
        ax = df[column].value_counts().rename(index=renamed_index_dict).plot.pie(colors=default_colors,
                                                                                 autopct='%1.1f%%', startangle=90,
                                                                                 title=title)
        ax.set_ylabel('')

        for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] + ax.get_xticklabels() + ax.get_yticklabels()):
            item.set_fontsize(20)

        centre_circle = plt.Circle((0, 0), 0.40, fc="white")
        fig.gca().add_artist(centre_circle)

    fig3 = plt.gcf()
    fig3.set_size_inches(15, 20)
    grid_rows = 5
    grid_cols = 2
    # fig3.patch.set_facecolor('white')
    # fig3.patch.set_facecolor('#82cfff')
    # fig3.patch.set_alpha(0.6)

    plt.subplot(grid_rows, grid_cols, 1)
    draw_semi_pie_chart(df, 'Sex', fig3, {0: 'Female', 1: 'Male'}, 'Sex')

    plt.subplot(grid_rows, grid_cols, 2)
    draw_semi_pie_chart(df, 'DiffWalking', fig3, {0: 'No', 1: 'Yes'}, 'DiffWalking')

    plt.subplot(grid_rows, grid_cols, 3)
    draw_semi_pie_chart(df, 'AlcoholDrinking', fig3, {0: 'No', 1: 'Yes'}, 'AlcoholDrinking')

    plt.subplot(grid_rows, grid_cols, 4)
    draw_semi_pie_chart(df, 'KidneyDisease', fig3, {0: 'No', 1: 'Yes'}, 'KidneyDisease')

    plt.subplot(grid_rows, grid_cols, 5)
    draw_semi_pie_chart(df, 'Asthma', fig3, {0: 'No', 1: 'Yes'}, 'Asthma')

    plt.subplot(grid_rows, grid_cols, 6)
    draw_semi_pie_chart(df, 'SkinCancer', fig3, {0: 'No', 1: 'Yes'}, 'SkinCancer')

    plt.subplot(grid_rows, grid_cols, 7)
    draw_semi_pie_chart(df, 'Stroke', fig3, {0: 'No', 1: 'Yes'}, 'Stroke')

    plt.subplot(grid_rows, grid_cols, 8)
    draw_semi_pie_chart(df, 'PhysicalActivity', fig3, {0: 'No', 1: 'Yes'}, 'PhysicalActivity')

    plt.subplot(grid_rows, grid_cols, 9)
    draw_semi_pie_chart(df, 'Smoking', fig3, {0: 'No', 1: 'Yes'}, 'Smoking')

    plt.subplot(grid_rows, grid_cols, 10)
    draw_semi_pie_chart(df, 'HeartDisease', fig3, {0: 'No', 1: 'Yes'}, 'HeartDisease')

    fig3.tight_layout(pad=4.0)
    st.pyplot(fig3)

    st.write("Visit this --> ", "[CDC website](https://www.cdc.gov/heartdisease/facts.htm)", "webpage to learn more "
                                                                                             "about HEART DISEASE "
                                                                                             "FACTS "
                                                                                             ":")
