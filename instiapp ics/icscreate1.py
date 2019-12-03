import datetime, string

time_table = {
		"1A": ['MO', '083000'],
		"2A": ['MO', '093000'],
		"3A": ['MO', '103500'],
		"4A": ['MO', '113500'],
		"8A": ['MO', '140000'],
		"9A": ['MO', '153000'],
		"12A": ['MO', '170500'],
		"13A": ['MO', '183500'],

		"4B": ['TU', '083000'],
		"1B": ['TU', '093000'],
		"2B": ['TU', '103500'],
		"3B": ['TU', '113500'],
		"10A": ['TU', '140000'],
		"11A": ['TU', '153000'],
		"14A": ['TU', '170500'],
		"15A": ['TU', '183500'],	

		"7A": ['WE', '083000'],
		"5A": ['WE', '093000'],
		"6A": ['WE', '110500'],
		"X1": ['WE', '140000'],
		"X2": ['WE', '150000'],
		"X3": ['WE', '160000'],
		"XC": ['WE', '170500'],
		"XD": ['WE', '183500'],

		"3C": ['TH', '083000'],
		"4C": ['TH', '093000'],
		"1C": ['TH', '103500'],
		"2C": ['TH', '113500'],
		"8B": ['TH', '140000'],
		"9B": ['TH', '153000'],
		"12B": ['TH', '170500'],
		"13B": ['TH', '183500'],	

		"7B": ['FR', '083000'],
		"5B": ['FR', '093000'],
		"6B": ['FR', '110500'],
		"10B": ['FR', '140000'],
		"11B": ['FR', '153000'],
		"14B": ['FR', '170500'],
		"15B": ['FR', '183500']
}

inp = input("Enter slot")
course = input("Enter course code")

date_today = str(datetime.date.today())
print(date_today.replace('-', ''))
day = time_table[inp]
dstart = "DTSTART:" + date_today.replace('-', '') + "T" + day[1]


# RRULE:FREQ=WEEKLY;BYDAY=SU,MO;INTERVAL=1
rrule = "RRULE:FREQ=WEEKLY;BYDAY=" + day[0] + ";INTERVAL=1"

f = open("demofile2.ics", "w")
f.write("BEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VEVENT\n{}\n".format(dstart))
f.write("{}\nDESCRIPTION: {}\nSEQUENCE:0\nSTATUS:CONFIRMED\nSUMMARY: {}\nTRANSP:OPAQUE\nEND:VEVENT".format(rrule,course,course))
f.write("\nEND:VCALENDAR")
f.close()