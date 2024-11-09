```python
# HOMEWORK 08-11-24

## Exercise_1_print_function
### *use the print function to type Hello World!"*

    print("Hello World!")

### *assign "Hello World!" to the variable my_text*

    my_text="Hello World!"
    print(my_text)

## E2_variables
### *Assign: 3 to variable glass_of_water*

    glass_of_water=3
    print("I drank", glass_of_water, "glasses of water today.")

### *Place the variable: glass_of_water inside the print function and observe what happens.*

    glass_of_water=glass_of_water + 1
    print(glass_of_water)

## E3_Data_types
### *Assign an integer to the variable, then print it.*

    men_stepped_on_the_moon=12
    print(men_stepped_on_the_moon)

### *Type a couple of words or a short sentence for your variable, then print it.*

    my_reason_for_coding="trying to further my knowledge with IT and its practical adaptations"
    print(my_reason_for_coding)

### *Assign a float with 2 decimals to the variable below. If you don't wan't to search the value you can check out Hint 1.*

    global_mean_sea_level_2018=21.36
    print(global_mean_sea_level_2018)

## E9_strings
### *Assign the string below the variable from the exercise.*

    str="It's always darkest before dawn"
    print(str)

### *Use first, second and last character of the string to make a new string.*
    str="It's always darkest before dawn."
    ans_1=str[0] + str[1] + str[-1]
    print(ans_1)

### *Replace the (.) with (!)*
    str="It's always darkest before dawn."
    str = str.replace(".", "!")
    print(str)

## E10_len_function
### *Using len() function find out how many items are in the list.*
    lst=[11, 10, 12, 101, 99, 1000, 999]
    answer_1=len(lst)
    print(answer_1)

### *Find out the length of the string given below.*
    msg="Be yourself, everyone else is taken."
    msg_length=len(msg)
    print(msg_length)

### *How many keys are there in the dictionary?*
    dict={"Real Madrid": 13,"AC Milan": 7,"Bayern Munich":5 ,"Barcelona": 5, "Liverpool": 5}
    ans_1=len(dict)
    print(ans_1)

## E11_Sort_method
### *Sort the list in ascending manner*
    lst=[11, 100, 99, 1000, 999]
    lst.sort()
    print(lst)

### *sort the countries in alphabetic order.*
    lst=["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]
    lst.sort()
    print(lst)

### *sort the list in descending order *
    lst=[11, 100, 101, 999, 1001]
    lst.sort(reverse=True)

## E12_Pop_method
### *Pop the last item of the list below.*
    lst=[11, 100, 99, 1000, 999]
    popped_item=lst.pop()
    print(popped_item)
    print(lst)

### *Remove "broccoli" from the list using .pop and .index methods.*
    lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]
    a=lst.index("broccoli")
    item=lst.pop(a)
    print(lst, item)

### *Save Italy's GDP in a separate variable and remove it from the dictionary.*
    GDP_2018={"US": 21, "China": 16, "Japan": 5, "Germany": 4, "India": 3, "France": 3, "UK": 3, "Italy": 2}
    italy_gdp=GDP_2018.pop("Italy")
    print(GDP_2018)
    print(italy_gdp, "trillion USD")
    ```