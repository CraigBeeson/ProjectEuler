monthsDays = {
	"january" : 31,
	"february" : 28,
	"march" : 31,
	"april" : 30,
	"may" : 31,
	"june" : 30,
	"july" : 31,
	"august" : 31,
	"september" : 30,
	"october" : 31,
	"november" : 30,
	"december" : 31,
}
months = ["january", "february", "march", "april", "may","june","july","august","september","october","november","december"]
year = 1901
day = 365
sundayCount = 0
while year <= 2000:
	for i in months:
		day += monthsDays[i]
		if i == "february":
			if year % 4 == 0:
				if year % 100 == 0:
					if year % 400 == 0:
						day += 1
				else:
					day += 1
		if day % 7 == 6:
			sundayCount += 1
	year += 1
print(sundayCount)