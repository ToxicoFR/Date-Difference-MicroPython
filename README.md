#Calculating the Difference Between Two Dates in MicroPython

#### Why ?
If you want to calculate the différence between two dates (in month, day, year...), in micropython you can use this program very easily 

### Params:
#### You must have two variables, one for the start date and the second for the end. The values must be in [year, month, day] so you can use utime.localtime to convert timestamp into this format
`startdate = utime.localtime(1616861486)
enddate = utime.localtime(1718295086)`
(for example)

### Get the difference in Day:
`differenceDay(d1, d2)`
### Get the difference in Months and Days:
`differenceMonthDay(d1, d2)`

### Get the difference in Years, Months and Days:
`differenceYearMonthDay(d1, d2)`

### Get the differences in Hours:
`differenceHours(d1,d2)`
