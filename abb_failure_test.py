# Global variables here

# Informational functions go here
def get_powercycle_ac():
    print("Use enter to advance")
    input("Open SLD")
    input("Start at inverter and move towards the left")
    input("Turn off the inverter")
    input("Turn off any AC disconnects")
    input("Turn off the PV breaker")
    input("Wait 10 seconds")
    input("Turn on the PV breaker")
    input("Turn on any AC disconnects")
    input("Turn on the inverter")

def get_production_confirmed():
    print("Production confirmed")

def get_production_status():
    production_status = input("Is the system producing now? ")
    production_status = production_status.lower()
    return production_status

def get_invalid_entry():
    print("Invalid entry -- Use yes or no")

def get_failure_note(sub_queue):
    print("Create a case to send to the field")
    print("Queue: System Failure")
    print("Sub-queue:", sub_queue)
    print("Case Owner: Field Service Technician")
    print("Flow Status: Remediation Ready")

def get_escalate_sd(sub_queue):
    print("Escalate this case to SD for an RMA")
    print("Queue: System Failure")
    print("Sub-queue:", sub_queue)
    print("Case Owner: Systems Diagnostics")
    print("Flow Status: Working in SD")

## Error code functions go here

# This is the blank display function
def get_blank_display():
    production_status = get_production_status()
    if production_status == "y" or production_status == "yes":
        get_production_confirmed()
    elif production_status == "n" or production_status == "no":
        get_failure_note("TBD")
    else:
        get_invalid_entry()
        get_blank_display()

# This is the E015 function
def get_e015():
    get_powercycle_ac()
    get_production_status()
    if production_status == "y" or production_status == "n" or production_status == "yes" or production_status == "no":
        valid_input = "true"
    else:
        valid_input = "false"
    while valid_input == "false":
        get_invalid_entry()
        get_production_status()
        if production_status == "y" or production_status == "n" or production_status == "yes" or \
                production_status == "no":
            valid_input = "true"
        else:
            valid_input = "false"
    if production_status == "y" or production_status == "yes":
        get_production_confirmed()
    else:
        get_escalate_sd("Defective Inverter")

# This is the E018 / Measuring Riso / Riso Low function
def get_abb_ground():
    trina = input("Are Trina modules preset? ")
    trina = trina.lower()
    if trina == "y" or trina == "n" or trina == "yes" or trina == "no":
        valid_trina = "true"
    else:
        valid_trina = "false"
    while valid_trina == "false":
        get_invalid_entry()
        trina = input("Are Trina modules preset? ")
        trina = trina.lower()
        if trina == "y" or trina == "n" or trina == "yes" or trina == "no":
            valid_trina = "true"
        else:
            valid_trina = "false"
    if trina == "y" or trina == "yes":
        print("Follow the defective Trina module Confluence page")
    else:
        print("Do not troubleshoot")
        get_failure_note("Ground Fault")

# This is basic ABB troubleshooting. Power cycle then to field
def get_basic():
    get_powercycle_ac()
    get_production_status()
    if production_status == "y" or production_status == "n" or production_status == "yes" or production_status == "no":
        valid_input = "true"
    else:
        valid_input = "false"
    while valid_input == "false":
        get_invalid_entry()
        get_production_status()
        if production_status == "y" or production_status == "n" or production_status == "yes" or \
                production_status == "no":
            valid_input = "true"
        else:
            valid_input = "false"
    if production_status == "y" or production_status == "yes":
        get_production_confirmed()
    else:
        get_failure_note("TBD")

# This is the E031 function
def get_e031():
    get_powercycle_ac()
    get_production_status()
    if production_status == "y" or production_status == "n" or production_status == "yes" or production_status == "no":
        valid_input = "true"
    else:
        valid_input = "false"
    while valid_input == "false":
        get_invalid_entry()
        get_production_status()
        if production_status == "y" or production_status == "n" or production_status == "yes" or \
                production_status == "no":
            valid_input = "true"
        else:
            valid_input = "false"
    if production_status == "y" or production_status == "yes":
        get_production_confirmed()
    else:
        week_code = input("Are the last two digits of the week code 14 or lower? ")
        week_code = week_code.lower()
        if week_code == "y" or week_code == "n" or week_code == "yes" or week_code == "no":
            valid_input = "true"
        else:
            valid_input = "false"
        while valid_input == "false":
            get_invalid_entry()
            week_code = input("Are the last two digits of the week code 14 or lower? ")
            week_code = week_code.lower()
            if week_code == "y" or week_code == "n" or week_code == "yes" or week_code == "no":
                valid_input = "true"
            else:
                valid_input = "false"
        if week_code == "y" or week_code == "yes":
            get_escalate_sd("Defective Inverter")
            print("*** Ensure you are including the MAC address of the defective inverter in your note ***")
            print("*** Ensure you are including the Serial Number of the defective inverter in your note ***")
        else:
            get_failure_note("Defective Inverter")

# This is the E033 / DSP COMM FAULT function
def get_abb_auto_rma():
    get_powercycle_ac()
    get_production_status()
    if production_status == "y" or production_status == "n" or production_status == "yes" or production_status == "no":
        valid_input = "true"
    else:
        valid_input = "false"
    while valid_input == "false":
        get_invalid_entry()
        get_production_status()
    if production_status == "y" or production_status == "n" or production_status == "yes" or production_status == "no":
        valid_input = "true"
    else:
        valid_input = "false"
    if production_status == "y" or production_status == "yes":
        get_production_confirmed()
    else:
        get_escalate_sd("Defective Inverter")

# This is the E050 and E053 ABB arc fault function
def get_arc():
    h4 = input("Is this job Amphenol / H4? ")
    h4 = h4.lower()
    if h4 == "y" or h4 == "n" or h4 == "yes" or h4 == "no":
        valid_input = "true"
    else:
        valid_input = "false"
    while valid_input == "false":
        get_invalid_entry()
        h4 = input("Is this job Amphenol / H4? ")
        h4 = h4.lower()
        if h4 == "y" or h4 == "n" or h4 == "yes" or h4 == "no":
            valid_input = "true"
        else:
            valid_input = "false"
    if h4 == "y" or h4 == "yes":
        print("Follow the Amphenol / H4 Confluence page ")
    else:
        print("Do not troubleshoot")
        get_failure_note("Arc Fault")

### The main ABB function
def get_abb_error_main():
    error_code = input("Please enter ABB error code: ")
    error_code = error_code.lower()
    if error_code == "blank" or error_code == "blank display":
        get_powercycle_ac()
        get_blank_display()
    elif error_code == "e013" or error_code == "013":
        get_basic()
    elif error_code == "e015" or error_code == "015":
        get_e015()
    elif error_code == "e018" or error_code == "018":
        get_abb_ground()
    elif error_code == "measuring riso":
        get_abb_ground()
    elif error_code == "riso low":
        get_abb_ground()
    elif error_code == "e019" or error_code == "019":
        get_basic()
    elif error_code == "e020" or error_code == "020":
        get_basic()
    elif error_code == "missing grid":
        get_basic()
    elif error_code == "e031" or error_code == "031":
        get_e031()
    elif error_code == "e033" or error_code == "033":
        get_abb_auto_rma()
    elif error_code == "DSP COMM FAULT":
        get_abb_auto_rma()
    elif error_code == "e050" or error_code == "050":
        get_arc()
    elif error_code == "e053" or error_code == "053":
        get_arc()
    else:
        print("Invalid entry -- Try again")
        get_abb_error_main()

# The main Fronius system failure function
def get_fronius_error_main():
    print("Hello, world!")
    error_code = input("Please enter Fronius error code: ")
    error_code = error_code.lower()

# Starts the main abb system failure
#get_abb_error_main()


# This is the main system failure page where you'll input the inverter type
# The input should bring you to the correct inverter troubleshooting function

# Defining the main function
def get_system_failure_main():
    inverter_type = input("Please enter the name of the inverter: ")
    inverter_type = inverter_type.lower()
    if inverter_type == "abb" or inverter_type == "fronius":
        valid_input = "true"
    else:
        valid_input = "false"
    while valid_input == "false":
        print("Invalid entry -- Only acceptable answers are: abb, fronius")
        inverter_type = input("Please enter the name of the inverter: ")
        if inverter_type == "abb" or inverter_type == "fronius":
            valid_input = "true"
        else:
            valid_input = "false"
    if inverter_type == "abb":
        get_abb_error_main()
    elif inverter_type == "fronius":
        get_fronius_error_main()

# Calling the main function
# This will ask for inverter input to take the user to the inverter specific troubleshooting
get_system_failure_main()
