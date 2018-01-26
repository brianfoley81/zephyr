from datetime import datetime


def normal_time(t):
	return datetime.fromtimestamp(int(t)).strftime('%Y-%m-%d %H:%M:%S')

f = open("./logs/fans.log")

info_lines = []

for line in f:
	if line.startswith("INFO"):
		info_lines.append(line)
f.close()

print ""
print ""

for line in info_lines:
	line = line.strip("\n")
	line = line.strip("\r")

	log_info = line.split(":")

	line = log_info[-1]

	line_data = line.split("||")

	line_stamp = line_data[0]
	line_c = line_data[1]
	line_f = str(( float(line_c) * (9.0/5.0)) + 32)
	line_h = line_data[2]


	print line_stamp + " | " + line_c + "C | " + line_f + "F | " + line_h + "% | " +  normal_time(line_stamp)

print ""
print ""