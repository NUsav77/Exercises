import csv

desired_wage = int
high_wages = []

with open('wage.csv', 'r') as infile:
    # Two steps required here
    reader = csv.reader(infile)  # 1. Create CSV reader
    next(reader)  # Consumes lines one at a time
    for row in reader:
        job_id = int(row[0])
        job_title = str(row[1])
        annual_wage = int(row[2])  # This gets the annual wage from
        # the integer version of row position 2


def get_desired_job():
    if annual_wage >= desired_wage:  # This takes all annual wages greater than desired
        high_wages.append(row)  # And appends the row


def print_jobs():
    for line in high_wages:
        print(line)


desired_wage = int(input('What is your desired wage: '))
print("List of possible jobs in your desired wage:\n")
get_desired_job()
