import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def fashion_product_data():

    ready_fashion_data = pd.read_csv("final_fashion_data.csv")
    print(ready_fashion_data.columns)

    dataframe = {'Product_name': [], 'Rating': [], 'Discount%': [], 'Reviews Count': [], 'Discounted_Price(₹)': [],
                 'Original_Price(₹)': []}

    '''Rate vise sort and create dataframe'''

    def star_rating_filter():
        print("\nFind Product with Rate Range.(e.g.: 2.5 to 4.3 Star rating Product)")
        star_rate = input("Enter Range Lower star:- ")
        star_rate1 = input("Enter Range Higher star:- ")

        data1 = pd.DataFrame(dataframe)
        no = 0

        for i in range(0, 2001):
            if (ready_fashion_data["Rating"][i] >= float(star_rate)) and (
                    ready_fashion_data["Rating"][i] <= float(star_rate1)):
                data2 = (ready_fashion_data.iloc[i:(i + 1), :])
                data1 = pd.concat([data1, data2], axis=0)  # concat is replacement of append to datafream
                no = no + 1

        print(data1["Rating"])
        print(data1.shape)

        '''draw pair plot and bar plot '''
        sns.pairplot(data1)
        plt.title(str(star_rate) + " to " + str(star_rate1) + " RANGE ")
        plt.show()

    '''select product as per price range'''

    def price_range_filter():
        print("\nFind product with Price Range(e.g.:- 500 to 1000)")
        lower_price = input("Enter Range Lower price:- ")
        higher_price = input("Enter Range Higher price:- ")

        data1 = pd.DataFrame(dataframe)
        no = 0

        for i in range(0, 2001):
            if (int(ready_fashion_data["Original_Price(₹)"][i]) >= int(lower_price)) and (
                    int(ready_fashion_data["Original_Price(₹)"][i]) <= int(higher_price)):
                data2 = (ready_fashion_data.iloc[i:(i + 1), :])
                data1 = pd.concat([data1, data2], axis=0)  # concat is replacement of append to dataframe
                no = no + 1

        print(data1["Original_Price(₹)"])
        print(data1.shape)

        '''draw pair plot and bar plot '''
        sns.pairplot(data1)
        plt.title(str(lower_price) + " to " + str(higher_price) + " RANGE ")
        plt.show()

    '''select product as per Name'''

    def product_name_filter():
        print("\nFind Product with Price Range")
        pro_name = input(str("Enter Product Name:- "))

        data1 = pd.DataFrame(dataframe)
        no = 0

        for i in range(0, 2001):
            if pro_name.lower() in (str(ready_fashion_data["Product_name"][i]).lower()):
                data2 = (ready_fashion_data.iloc[i:(i + 1), :])
                data1 = pd.concat([data1, data2], axis=0)  # concat is replacement of append to datafream
                no = no + 1

        print(data1["Product_name"])
        print(data1.shape)

        '''draw pair plot and bar plot '''
        sns.pairplot(data1)
        plt.title(pro_name.upper())
        plt.show()

    print("Hello,\nHere select option and get filter products and visualize.")
    print('''------Filter Option------\nOption 0 >>> Exit\nOption 1 >>> Price Range Filter\nOption 2 >>> Star Rating Filter\nOption 3 >>> Product Name Filter''')

    while True:
        filter_option = int(input("\nEnter Filter option:- "))
        if filter_option == 1:
            price_range_filter()

        elif filter_option == 2:
            star_rating_filter()

        elif filter_option == 3:
            product_name_filter()

        elif filter_option == 0:
            print("Hope, You get your Answer")
            break

        else:
            print("Enter Valid Option")

'''Part 1 for sheet 1  electronic products data'''

def first_electronic_product_data():

    ele_prod_data = pd.read_csv("final_ele_data.csv")
    print(ele_prod_data.columns)
    print(ele_prod_data.shape)

    dataframe = {'Title': [], 'Rating': [], 'Discount%': [], 'Discounted_Price(₹)': [],
                 'Original_Price(₹)': []}

    '''Rate vise sort and create dataframe'''

    def star_rating_filter():

        print("\nFind Product with Rate Range.(e.g.: 2.5 to 4.3 Star rating Product)")
        star_rate = input("Enter Range Lower star:- ")
        star_rate1 = input("Enter Range Higher star:- ")

        data1 = pd.DataFrame(dataframe)
        no = 0

        for i in range(0, 1445):
            if (ele_prod_data["Rating"][i] >= float(star_rate)) and (ele_prod_data["Rating"][i] <= float(star_rate1)):
                data2 = (ele_prod_data.iloc[i:(i + 1), :])
                data1 = pd.concat([data1, data2], axis=0)  # concat is replacement of append to datafream
                no = no + 1

        print(data1["Rating"])
        print(data1.shape)

        '''draw pair plot and bar plot '''
        sns.pairplot(data1)
        plt.title(str(star_rate) + " to " + str(star_rate1) + " RANGE ")
        plt.show()

    '''select product as per price range'''

    def price_range_filter():

        print("\nFind product with Price Range(e.g.:- 500 to 1000)")
        lower_price = input("Enter Range Lower price:- ")
        higher_price = input("Enter Range Higher price:- ")

        data1 = pd.DataFrame(dataframe)
        no = 0

        for i in range(0, 1445):
            if (int(ele_prod_data["Original_Price(₹)"][i]) >= int(lower_price)) and (
                    int(ele_prod_data["Original_Price(₹)"][i]) <= int(higher_price)):
                data2 = (ele_prod_data.iloc[i:(i + 1), :])
                data1 = pd.concat([data1, data2], axis=0)  # concat is replacement of append to dataframe
                no = no + 1

        print(data1["Original_Price(₹)"])
        print(data1.shape)

        '''draw pair plot and bar plot '''
        sns.pairplot(data1)
        plt.title(str(lower_price)+" to "+str(higher_price)+" RANGE ")
        plt.show()

    '''select product as per Name'''

    def product_name_filter():
        print("\nFind Product by Name")
        pro_name = input(str("Enter Product Name:- "))

        data1 = pd.DataFrame(dataframe)
        no = 0

        for i in range(0, 1445):
            if pro_name.lower() in (str(ele_prod_data["Title"][i]).lower()):
                data2 = (ele_prod_data.iloc[i:(i + 1), :])
                data1 = pd.concat([data1, data2], axis=0)  # concat is replacement of append to datafream
                no = no + 1

        print(data1["Title"])
        print(data1.shape)
        print(data1.describe())

        '''draw pair plot and bar plot '''
        sns.pairplot(data1)
        plt.title(pro_name.upper())
        plt.show()

    print("Hello,\nHere select option and get filter products and visualize.")
    print('''------Filter Option------\nOption 0 >>> Exit\nOption 1 >>> Price Range Filter\nOption 2 >>> Star Rating Filter\nOption 3 >>> Product Name Filter''')

    while True:
        filter_option = int(input("\nEnter Filter option:- "))
        if filter_option == 1:
            price_range_filter()

        elif filter_option == 2:
            star_rating_filter()

        elif filter_option == 3:
            product_name_filter()

        elif filter_option == 0:
            print("Hope, You get your Answer")
            break

        else:
            print("Enter Valid Option")


'''Part 2 for sheet 2 electronic products data'''
def second_electronic_product_data():
    ele_prod_data = pd.read_csv("final_ele2_data.csv")
    print(ele_prod_data.columns)
    print(ele_prod_data.shape)

    dataframe = {'Title': [], 'Rating': [], 'Discount%': [], 'Discounted_Price(₹)': [],
                 'Original_Price(₹)': []}

    '''Rate vise sort and create dataframe'''

    def star_rating_filter():

        print("\nFind Product with Rate Range.(e.g.: 2.5 to 4.3 Star rating Product)")
        star_rate = input("Enter Range Lower star:- ")
        star_rate1 = input("Enter Range Higher star:- ")

        data1 = pd.DataFrame(dataframe)
        no = 0

        for i in range(0, 1180):
            if (ele_prod_data["Rating"][i] >= float(star_rate)) and (ele_prod_data["Rating"][i] <= float(star_rate1)):
                data2 = (ele_prod_data.iloc[i:(i + 1), :])
                data1 = pd.concat([data1, data2], axis=0)  # concat is replacement of append to datafream
                no = no + 1

        print(data1["Rating"])
        print(data1.shape)

        '''draw pair plot and bar plot '''
        sns.pairplot(data1)
        plt.title(str(star_rate) + " to " + str(star_rate1) + " RANGE ")
        plt.show()

    '''select product as per price range'''

    def price_range_filter():

        print("\nFind product with Price Range(e.g.:- 500 to 1000)")
        lower_price = input("Enter Range Lower price:- ")
        higher_price = input("Enter Range Higher price:- ")

        data1 = pd.DataFrame(dataframe)
        no = 0

        for i in range(0, 1180):
            if (int(ele_prod_data["Original_Price(₹)"][i]) >= int(lower_price)) and (
                    int(ele_prod_data["Original_Price(₹)"][i]) <= int(higher_price)):
                data2 = (ele_prod_data.iloc[i:(i + 1), :])
                data1 = pd.concat([data1, data2], axis=0)  # concat is replacement of append to dataframe
                no = no + 1

        print(data1["Original_Price(₹)"])
        print(data1.shape)

        '''draw pair plot and bar plot '''
        sns.pairplot(data1)
        plt.title(str(lower_price) + " to " + str(higher_price) + " RANGE ")
        plt.show()

    '''select product as per Name'''

    def product_name_filter():
        print("\nFind Product by Name")
        pro_name = input(str("Enter Product Name:- "))

        data1 = pd.DataFrame(dataframe)
        no = 0

        for i in range(0, 1180):
            if pro_name.lower() in (str(ele_prod_data["Title"][i]).lower()):
                data2 = (ele_prod_data.iloc[i:(i + 1), :])
                data1 = pd.concat([data1, data2], axis=0)  # concat is replacement of append to datafream
                no = no + 1

        print(data1["Title"])
        print(data1.shape)
        print(data1.describe())

        '''draw pair plot and bar plot '''
        sns.pairplot(data1)
        plt.title(pro_name.upper())
        plt.show()

    print("Hello,\nHere select option and get filter products and visualize.")
    print('''------Filter Option------\nOption 0 >>> Exit\nOption 1 >>> Price Range Filter\nOption 2 >>> Star Rating Filter\nOption 3 >>> Product Name Filter''')

    while True:
        filter_option = int(input("\nEnter Filter option:- "))
        if filter_option == 1:
            price_range_filter()

        elif filter_option == 2:
            star_rating_filter()

        elif filter_option == 3:
            product_name_filter()

        elif filter_option == 0:
            print("Hope, You get your Answer")
            break

        else:
            print("Enter Valid Option")

print("\n----EDA for Amezon Data----")
# print('''------Filter Option------\nOption 0 >>> Exit\nOption 1 >>> Fashion Product\nOption 2 >>> Electronic Data(sheet 1)\nOption 3 >>> Electronic Data(sheet 2)''')

while True:
    print('''------Filter Option------\nOption 0 >>> Exit\nOption 1 >>> Fashion Product\nOption 2 >>> Electronic Data(sheet 1)\nOption 3 >>> Electronic Data(sheet 2)''')

    data_no = int(input("\nEnter No:- "))
    if data_no == 1:
        print("Fashion Product")
        fashion_product_data()

    elif data_no == 2:
        print("Electronic Data(sheet 1)")
        first_electronic_product_data()

    elif data_no == 3:
        print("Electronic Data(sheet 2)")
        second_electronic_product_data()

    elif data_no == 0:
        print("Hope, You get your Answer")
        break

    else:
        print("Enter Valid Option")
