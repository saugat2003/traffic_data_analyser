"""
****************************************************************************
Additional info
 1. I declare that my work contins no examples of misconduct, such as
 plagiarism, or collusion.
 2. Any code taken from other sources is referenced within my code solution.
 3. Saugat Bhattarai
 4. Date: 11/24/2024
****************************************************************************

"""
## =========================== Importing necessary libraries ==============================
from graphics import *
import csv
import math


### ------------------------------- Take input from User and Validate Date --------------------------------
def date_validator():
    while True:
        try:
            # Taking date as a input in range of 1 to 31
            day = int(input("Please enter the day of the survey in the format dd: "))
            if not (1 <= day <= 31):
                print("Out of range - values must be in the range 1 and 31.")
                continue
            
            # Taking month as a input and validate it.
            month = int(input("Please enter the month of the survey in the format MM: "))
            if not (1 <= month <= 12):
                print("Out of range - values must be in the range 1 and 12.")
                continue
            
            # Taking year as a input and validate it.
            year = int(input("Please enter the year of the survey in the format YYYY: "))
            if not (2000 <= year <= 2024):
                print("Out of range - values must range from 2000 and 2024.")
                continue
                
            # Return day month and year in a required format.
            return f"{day:02d}{month:02d}{year}"
        
        # Error handeling if the user input string it gives error
        except ValueError:
            print("Integer required.")

# --------------------------------------- Processing the csv file data ------------------------
def processed_csv_data(csv_file_name):
    # Opening csv file in read mode as a file.
    with open(csv_file_name , "r") as file:
        lines = file.readlines()   # readlines() provides all the lines in the file as a list of strings. 
        data = [line.strip().split(',') for line in lines[1:]] # removing white space, seperate by commas and exclude header.

    try:
        # ================= Counters starting from zero to count required value =========================
        total_vehicles = len(data)
        total_trucks = 0
        total_electric = 0
        total_two_wheeled = 0
        total_busses_north = 0
        total_not_turning = 0
        total_speed_limit_exceeded = 0
        elm_rabbit_count = 0
        hanley_westway_count = 0
        elm_rabbit_scooters = 0
        hanley_hours = [0] * 24
        rain_hours_set = set()  # Track unique hours of rain
        bicycles_per_hour = [0] * 24

        # ===================  For csv_record data's to count required values =========================================
        for record in data:
            junction_name = record[0]
            date = record[1]
            time_of_day = record[2]
            travel_in = record[3]
            travel_out = record[4]
            weather = record[5]
            speed_limit = int(record[6])
            vehicle_speed = int(record[7])
            vehicle_type = record[8]
            electric_hybrid = record[9] == 'True'

        # ======================== Updating counter according to question ================
            if vehicle_type == 'Truck':
                total_trucks += 1
            if electric_hybrid:
                total_electric += 1
            if vehicle_type in ['Bicycle', 'Motorcycle', 'Scooter']:
                total_two_wheeled += 1
            if junction_name == 'Elm Avenue/Rabbit Road' and vehicle_type == 'Buss' and travel_out == 'N':
                total_busses_north += 1
            if travel_in == travel_out:
                total_not_turning += 1
            if vehicle_speed > speed_limit:
                total_speed_limit_exceeded += 1
            if junction_name == 'Elm Avenue/Rabbit Road':
                elm_rabbit_count += 1
            if junction_name == 'Hanley Highway/Westway':
                hanley_westway_count += 1
                hour = int(time_of_day.split(':')[0])
                hanley_hours[hour] += 1
            if vehicle_type == 'Bicycle':
                hour = int(time_of_day.split(':')[0])
                bicycles_per_hour[hour] += 1
            if weather in ['Light Rain', 'Heavy Rain']:
                hour = int(time_of_day.split(":")[0])      
                rain_hours_set.add(hour)                   
            if junction_name == "Elm Avenue/Rabbit Road":
                if vehicle_type == 'Scooter':
                    elm_rabbit_scooters += 1

        # ========================== Calculate Percentages as well as average and rain hour  ===================================
        percentage_trucks = round((total_trucks / total_vehicles) * 100)
        percentage_scooters = round((elm_rabbit_scooters / elm_rabbit_count) * 100) if elm_rabbit_count > 0 else 0
        avg_bicycles_per_hour = round(sum(bicycles_per_hour) / 24)
        rain_hours = len(rain_hours_set)


        #===========================Find peak hours for Hanley Highway/Westway====================================
        peak_traffic = max(hanley_hours)
        peak_hours = [f"Between {hour:02d}:00 and {hour + 1:02d}:00" for hour, count in enumerate(hanley_hours) 
        if count == peak_traffic]


        #================================================= Display result ============================================
        results = [] #Initializing the empty list which will store the results and later it is used to paste.
        results.append(f"Data file selected is {csv_file_name}")
        results.append(f"The total number of vehicles recorded for this date is {total_vehicles}")
        results.append(f"The total number of trucks recorded for this date is {total_trucks}")
        results.append(f"The total number of electric vehicles for this date is {total_electric}")
        results.append(f"The total number of two-wheeled vehicles for this date is {total_two_wheeled}")
        results.append(f"The total number of Busses leaving Elm Avenue/Rabbit Road heading North is {total_busses_north}")
        results.append(f"The total number of Vehicles through both junctions not turning left or right is  {total_not_turning}")
        results.append(f"The percentage of all vehicles recorded that are trucks for this date is {percentage_trucks}%")
        results.append(f"The average number of Bikes per hour for this date is {avg_bicycles_per_hour}")
        results.append(f"The total number of vehicles recorded as over the speed limit for this date is {total_speed_limit_exceeded}")
        results.append(f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {elm_rabbit_count}")
        results.append(f"The total number of vehicles recorded through Hanley Highway/Westway junction is {hanley_westway_count}")
        results.append(f"The percentage of vehicles through Elm Avenue/Rabbit Road that are Scooters is {percentage_scooters}%")
        results.append(f"The highest number of vehicles in an hour on Hanley Highway/Westway is {peak_traffic}")
        results.append(f"The peak traffic hours are: {', '.join(peak_hours)}")
        results.append(f"The total number of hours of rain for this date is {rain_hours}")

        
        for result in results:
            print(result)
        # ---------- Error handeling --------------
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    return "\n".join(results)

#---------------------------------------- Opening csv File -----------------------
def opening_csv_file(csv_file_name):
    try:
        with open(csv_file_name, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{csv_file_name}' was not found. Please check the file name and path.")
        return None  # Return None to indicate failure
    data = [line.strip().split(',') for line in lines[1:]]
    return data


# ================================================================Histogram Starts ======================================
def draw_histogram(file_data, date):
    # -------------------------- Create a graphics window with adjusted size -------------------------------------------
    win = GraphWin("Histogram", 1200, 700)                # Width and Height
    win.setCoords(-2, 0, 25, 70)                          # Margin for better Spacing

    # ------------------Title with improved style -----------------------------
    title = Text(Point(12.5, 65), f"Histogram of Vehicle Frequency per Hour ({date[:2]}/{date[2:4]}/{date[4:]})")
    title.setSize(18)           # Title size
    title.setStyle("bold")
    title.setTextColor("blue")  # Title color
    title.draw(win)

    # ----------------- X-axis label -----------------------------------------
    x_label = Text(Point(12.5, 2), "Hours of the Day (00:00 to 23:00)")
    x_label.setSize(14)
    x_label.setStyle("bold")                # label size
    x_label.setTextColor("darkgreen")  # label color
    x_label.draw(win)

    # ----------------- Y-axis label -----------------------------------------
    # y_label = Text(Point(-1.5, 35), "Vehicle Count")
    # y_label.setSize(12)                # label size
    # y_label.setStyle("bold")
    # y_label.setTextColor("darkgreen")  # label color
    # y_label.draw(win)

    # ----------------- Draw X-axis and Y-axis lines ------------------------
    x_axis = Line(Point(0, 5), Point(24, 5))  # X-axis
    y_axis = Line(Point(0, 5), Point(0, 65))  # Y-axis
    x_axis.setWidth(2)
    y_axis.setWidth(2)
    x_axis.draw(win)
    y_axis.draw(win)

    # -----------------Adding X-axis tick marks and labels -----------------
    for hour in range(24):
        tick = Line(Point(hour + 0.5, 5), Point(hour + 0.5, 4.8))  # Tick mark
        tick.draw(win)
        hour_label = Text(Point(hour + 0.5, 4), f"{hour:02d}")  # Hour label
        hour_label.setSize(10)
        hour_label.draw(win)


    # --------------- Process data: Calculate hourly counts for both junctions-----------
    elm_rabbit_hours = [0] * 24                  # Hourly count for Elm Avenue/Rabbit Road
    hanley_westway_hours = [0] * 24              # Hourly count for Hanley Highway/Westway

    for record in file_data:
        time_of_day = record[2]
        hour = int(time_of_day.split(":")[0])    # Extract hour
        junction_name = record[0]

        if junction_name == "Elm Avenue/Rabbit Road":
            elm_rabbit_hours[hour] += 1
        elif junction_name == "Hanley Highway/Westway":
            hanley_westway_hours[hour] += 1

    # ------------------- Normalize bar height if counts are too high ----------------------------------
    max_count = max(max(elm_rabbit_hours), max(hanley_westway_hours))
    scale_factor = 1 if max_count <= 50 else 50 / max_count             # Scale bars to fit in the window

       #---------------- Adding Y-axis tick marks and labels -----------------
    for i in range(0, 51, 10):                                          # Labels every 10 units
       tick = Line(Point(-0.2, 5 + i), Point(0, 5 + i))                # Tick mark
       tick.draw(win)
       y_label = Text(Point(-1, 5 + i), str(int(i / scale_factor)))    # Y-axis label
       y_label.setSize(10)
       y_label.draw(win)

    #-------------------- Draw histogram bars for both junctions ---------------------------------------
    bar_width = 0.4                                                                     # Width of each bar
    for hour in range(24):
        #_________________________________Elm Avenue/Rabbit Road bars___________________________________
        elm_count = elm_rabbit_hours[hour]
        scaled_elm_count = elm_count * scale_factor
        elm_bar = Rectangle(Point(hour + 0.1, 5), Point(hour + 0.5, 5 + scaled_elm_count))  # Adjust position
        elm_bar.setFill("green")
        elm_bar.setOutline("black")
        elm_bar.setWidth(1.2)
        elm_bar.draw(win)

        #________________________________Hanley Highway/Westway bars____________________________________
        hanley_count = hanley_westway_hours[hour]
        scaled_hanley_count = hanley_count * scale_factor
        hanley_bar = Rectangle(Point(hour + 0.5, 5), Point(hour + 0.9, 5 + scaled_hanley_count))  # Adjust position
        hanley_bar.setFill("red")
        hanley_bar.setOutline("black")
        hanley_bar.setWidth(1.2)
        hanley_bar.draw(win)

        #------------------------------Display counts above bars for both junctions----------------------
        if elm_count > 0:
            elm_label = Text(Point(hour + 0.3, 5 + scaled_elm_count + 1), str(elm_count))
            elm_label.setSize(8)
            elm_label.setTextColor("black")
            elm_label.setStyle("bold")
            elm_label.draw(win)

        if hanley_count > 0:
            hanley_label = Text(Point(hour + 0.7, 5 + scaled_hanley_count + 1), str(hanley_count))
            hanley_label.setSize(8)
            hanley_label.setTextColor("black")
            hanley_label.setStyle("bold")
            hanley_label.draw(win)

    
    #----------------------Legend boxes and labels aligned in top right corner with padding--------------
    legend_x = 50                                   # Right side position
    legend_y = 45                                   # Top position with padding
    legend_title = Text(Point(13.25, 59.5), "Legend")
    legend_title.setSize(14)
    legend_title.setStyle("bold")
    legend_title.draw(win)

    #--------------------- First legend item (Elm Avenue/Rabbit Road)-------------------------------------
    legend_box1 = Rectangle(Point(10, 56), Point(10.5, 56.5))
    legend_box1.setFill("green")
    legend_box1.setOutline("black")
    legend_box1.draw(win)
    legend_label1 = Text(Point(13.5, 56.25), "Elm Avenue/Rabbit Road")
    legend_label1.setStyle("bold")
    legend_label1.setSize(10)
    legend_label1.draw(win)

    #----------------------- Second legend item (Hanley Highway/Westway) ---------------------------------
    legend_box2 = Rectangle(Point(10, 54.5), Point(10.5, 55))
    legend_box2.setFill("red")
    legend_box2.setOutline("black")
    legend_box2.draw(win)
    legend_label2 = Text(Point(13.5, 54.75), "Hanley Highway/Westway")
    legend_label2.setStyle("bold")
    legend_label2.setSize(10)
    legend_label2.draw(win)

    #-----------------------Waiting to close the window ----------------------------------------------------
    if win.isOpen():  
        win.getMouse()              # Wait for a mouse click
    win.close()                     # Close the window after the click

# ===========================================      Histogram end      =========================================

# =========================================== Write a file of results ==========================================
def write_results(results, csv_file_name):
    if results is None:                     # Check if results is None
        print("No results to write.")
        return False

    try:
        with open("results.txt", "a") as file:
            file.write(f"====================== Results for {csv_file_name} ===================== \n\n {results}\n")
            file.write("\n------------------------------------------------------------------------------------\n\n")
    except Exception as e:
        print(f"Error writing to file: {e}")
        raise

# -------------------------------------------- Take input in a Loop ----------------------------------
def main():
    while True:
        date = date_validator()
        csv_file_name = f"traffic_data{date}.csv"
        results = processed_csv_data(csv_file_name)
        write_results(results, csv_file_name)
        file_data = opening_csv_file(csv_file_name)
        draw_histogram(file_data, date)
            
        while True:
           user_input = input("Do you want to select another data file for a different date? Y/N: ").upper()
           if user_input == 'N':
               print("Program Exit!")
               return                                                           # Exit the program
           elif user_input == 'Y':
               break                                                            # Restart the loop for a new date
           else:
               print("Invalid input. Please enter Y or N.")

if __name__ == "__main__":
    main()
