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

def get_escalate_case(team, sub_queue):
    print("Escalate this case to " + team + " for an RMA")
    print("Queue: System Failure")
    print("Sub-queue:", sub_queue)
    print("Case Owner: " + team)
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
    production_status = get_production_status()
    if production_status == "y" or production_status == "n" or production_status == "yes" or production_status == "no":
        valid_input = "true"
    else:
        valid_input = "false"
    while valid_input == "false":
        get_invalid_entry()
        production_status = get_production_status()
        if production_status == "y" or production_status == "n" or production_status == "yes" or \
                production_status == "no":
            valid_input = "true"
        else:
            valid_input = "false"
    if production_status == "y" or production_status == "yes":
        get_production_confirmed()
    else:
        get_escalate_case("Systems Diagnostics", "Defective Inverter")

# This is the E018 / Measuring Riso / Riso Low function
def get_ground():
    trina = input("Are Trina modules present? ")
    trina = trina.lower()
    if trina == "y" or trina == "n" or trina == "yes" or trina == "no":
        valid_trina = "true"
    else:
        valid_trina = "false"
    while valid_trina == "false":
        get_invalid_entry()
        trina = input("Are Trina modules present? ")
        trina = trina.lower()
        if trina == "y" or trina == "n" or trina == "yes" or trina == "no":
            valid_trina = "true"
        else:
            valid_trina = "false"
    if trina == "y" or trina == "yes":
        print("Follow the defective Trina module Confluence page")
    else:
        print("Do not troubleshoot")
        print("Get the MΩ reading and document in the case notes")
        get_failure_note("Ground Fault")

# This is basic ABB troubleshooting. Power cycle then to field
def get_basic():
    get_powercycle_ac()
    production_status = get_production_status()
    if production_status == "y" or production_status == "n" or production_status == "yes" or production_status == "no":
        valid_input = "true"
    else:
        valid_input = "false"
    while valid_input == "false":
        get_invalid_entry()
        production_status = get_production_status()
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
    production_status = get_production_status()
    if production_status == "y" or production_status == "n" or production_status == "yes" or production_status == "no":
        valid_input = "true"
    else:
        valid_input = "false"
    while valid_input == "false":
        get_invalid_entry()
        production_status = get_production_status()
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
            get_escalate_case("TBA CTS", "Defective Inverter")
            print("*** Ensure you are including the MAC address of the defective inverter in your note ***")
            print("*** Ensure you are including the Serial Number of the defective inverter in your note ***")
        else:
            get_failure_note("Defective Inverter")

# This is the DSP COMM FAULT function
# I need to check on what DSP COMM FAULT process actually is
def get_abb_auto_rma():
    get_powercycle_ac()
    production_status = get_production_status()
    if production_status == "y" or production_status == "n" or production_status == "yes" or production_status == "no":
        valid_input = "true"
    else:
        valid_input = "false"
    while valid_input == "false":
        get_invalid_entry()
        production_status = get_production_status()
        if production_status == "y" or production_status == "n" or production_status == "yes" or production_status == "no":
            valid_input = "true"
        else:
            valid_input = "false"
    if production_status == "y" or production_status == "yes":
        get_production_confirmed()
    else:
        get_escalate_case("Systems Diagnostics", "Defective Inverter")

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

# This is the auto-RMA for SolarEdge HW error
def get_hw_error():
    get_powercycle_ac()
    production_status = get_production_status()
    if production_status == "y" or production_status == "n" or production_status == "yes" or production_status == "no":
        valid_input = "true"
    else:
        valid_input = "false"
    while valid_input == "false":
        get_invalid_entry()
        production_status = get_production_status()
        if production_status == "y" or production_status == "n" or production_status == "yes" or production_status == "no":
            valid_input = "true"
        else:
            valid_input = "false"
    if production_status == "y" or production_status == "yes":
        get_production_confirmed()
    else:
        get_escalate_case("Systems Diagnostics", "Defective Inverter")
        print("Get a clear picture of the error code and inverter serial number")
        print("Put both the pictures in the Maintenance folder under the caseID")

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
        get_ground()
    elif error_code == "measuring riso":
        get_ground()
    elif error_code == "riso low":
        get_ground()
    elif error_code == "e019" or error_code == "019":
        get_basic()
    elif error_code == "e020" or error_code == "020":
        get_basic()
    elif error_code == "missing grid":
        get_basic()
    elif error_code == "e031" or error_code == "031":
        get_e031()
    elif error_code == "e033" or error_code == "033":
        get_basic()
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
    error_code = input("Please enter Fronius error code: ")
    error_code = error_code.lower()
    if error_code == "blank" or error_code == "blank display":
        get_powercycle_ac()
        get_blank_display()
    elif error_code == "state 107" or error_code == "107":
        get_basic()
    elif error_code == "state 109" or error_code == "109":
        get_basic()
    elif error_code == "state 112" or error_code == "112":
        get_basic()
    elif error_code == "state 207" or error_code == "207":
        get_basic()
    elif error_code == "state 221" or error_code == "221":
        get_basic()
    elif error_code == "state 222" or error_code == "222":
        get_basic()
    elif error_code == "state 223" or error_code == "223":
        get_basic()
    elif error_code == "state 225" or error_code == "225":
        get_basic()
    elif error_code == "state 240" or error_code == "240":
        get_arc()
    elif error_code == "state 241" or error_code == "241":
        get_arc()
    elif error_code == "state 247" or error_code == "247":
        get_basic()
    elif error_code == "state 434" or error_code == "434":
        get_ground()
    elif error_code == "state 472" or error_code == "472":
        get_ground()
    elif error_code == "state 446" or error_code == "446":
        get_basic()
    elif error_code == "state 514" or error_code == "514":
        get_basic()
    elif error_code == "state 515" or error_code == "515":
        get_basic()
    elif error_code == "state 516" or error_code == "516":
        get_basic()
    elif error_code == "state 517" or error_code == "617":
        get_basic()
    elif error_code == "state 556" or error_code == "556":
        get_basic()
    else:
        print("Invalid entry -- Try again")
        get_fronius_error_main()

# The main SMA system failure function
def get_sma_error_main():
    error_code = input("Please enter SMA error code: ")
    error_code = error_code.lower()
    if error_code == "blank display" or error_code == "blank":
        get_powercycle_ac()
        get_blank_display()
    elif error_code == "disturbance earthcurmax" or error_code == "earthcurmax":
        get_ground()
    elif error_code == "disturbance gfdi fuse open" or error_code == "gfdi fuse open":
        get_ground()
    elif error_code == "disturbance fac-bfr" or error_code == "fac bfr" or error_code == "fac-bfr":
        get_basic()
    elif error_code == "disturbance vac-bfr" or error_code == "vac bfr" or error_code == "vac-bfr":
        get_basic()
    else:
        print("Invalid entry -- Try again")
        get_sma_error_main()

# The main SolarEdge system failure function
def get_solaredge_error_main():
    error_code = input("Please enter SolarEdge error code: ")
    error_code = error_code.lower()
    if error_code == "blank display" or error_code == "blank":
        get_powercycle_ac()
        get_blank_display()
    elif error_code == "error 147" or error_code == "147" or error_code == "error 150" or error_code == "150"\
            or error_code == "error 151" or error_code == "error 152" or error_code == "152" \
            or error_code == "error 3x11" or error_code == "3x11" or error_code == "error 2x96" or error_code == "2x96"\
            or error_code == "error 2x98" or error_code == "2x98" or error_code == "error 18xc" or error_code == "18xc":
        get_arc()
    elif error_code == "error 25" or error_code == "25" or error_code == "error 2x19" or error_code == "2x19":
        get_ground()
    elif error_code == "error 45sw" or error_code == "45sw" or error_code == "error 2x99" or error_code == "2x99":
        get_basic()
    elif error_code == "night mode" or error_code == "night":
        get_basic()
    elif error_code == "pac 0.0" or error_code == "pac 0" or error_code == "0.0" or error_code == "pac 00":
        get_basic()
    elif error_code == "18xb5" or error_code == "18xb5-9" or error_code == "18xb6" or error_code == "18xb7"\
            or error_code == "18xb8" or error_code == "18xb9" or error_code == "18xba" or error_code == "18xbc"\
            or error_code == "18xbd" or error_code == "error 28" or error_code == "28" or error_code == "2x1a"\
            or error_code == "2x1c" or error_code == "8x56" or error_code == "18x7b":
        get_hw_error()
    else:
        print("Invalid entry -- Try again")
        get_solaredge_error_main()

# The main Xantrex / Schneider / Delta system failure function
# Delta may need it's own in the future
def get_delta_error_main():
    error_code = input("Please enter the error code: ")
    error_code = error_code.lower()
    if error_code == "ac voltage fault" or error_code == "voltage fault":
        get_basic()
    elif error_code == "ground fault" or error_code == "ground":
        get_ground()
    elif error_code == "inverter offline" or error_code == "offline":
        get_basic()
    else:
        print("Invalid entry -- Try again")
        get_delta_error_main()

# Starts the main abb system failure
#get_abb_error_main()


# This is the main system failure page where you'll input the inverter type
# The input should bring you to the correct inverter troubleshooting function

# Defining the main function
def get_system_failure_main():
    inverter_type = input("Please enter the name of the inverter: ")
    inverter_type = inverter_type.lower()
    if inverter_type == "abb" or inverter_type == "fronius" or inverter_type == "sma"\
            or inverter_type == "solaredge":
        valid_input = "true"
    else:
        valid_input = "false"
    while valid_input == "false":
        print("Invalid entry -- Only acceptable answers are: abb, fronius, sma, solaredge")
        inverter_type = input("Please enter the name of the inverter: ")
        if inverter_type == "abb" or inverter_type == "fronius" or inverter_type == "sma"\
                or inverter_type == "solaredge":
            valid_input = "true"
        else:
            valid_input = "false"
    if inverter_type == "abb":
        get_abb_error_main()
    elif inverter_type == "fronius":
        get_fronius_error_main()
    elif inverter_type == "sma":
        get_sma_error_main()
    elif inverter_type == "solaredge":
        get_solaredge_error_main()
    elif inverter_type == "xantrex" or inverter_type == "schneider" or inverter_type == "delta":
        get_delta_error_main()

# Calling the main function
# This will ask for inverter input to take the user to the inverter specific troubleshooting

sentinel = False
while sentinel == False:
    print("This is a work in progress...")
    print("Please send any corrections, errors, feedback or improvements to kekislowski@tesla.com")
    troubleshoot = input("Would you like to troubleshoot a system failure? ")
    troubleshoot = troubleshoot.lower()
    if troubleshoot == "yes" or troubleshoot == "y":
        get_system_failure_main()
    elif troubleshoot == "no" or troubleshoot == "n":
        sentinel = True
        print("Goodbye!")
    else:
        print("Invalid Entry -- Select yes or no")