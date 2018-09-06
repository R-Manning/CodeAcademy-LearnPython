"""The program does the following:

Prompt the user to select a shape.
Calculate the area of that shape.
Print the area of that shape to the user."""

print('Calculator is starting.')

shape = raw_input("Enter C for Circle or T for Triangle: ")

if shape == 'C':
  radius = float(raw_input('Enter radius: '))
  area = 3.14159 * (radius**2)
  print('Area of circle is %f'%(area))
elif shape == 'T':
  base = float(raw_input('Enter base: '))
  height = float(raw_input('Enter height: '))
  area = 0.5 * base * height
  print('Area of triangle is %f'%(area))
else:
  print('You have entered an invalid shape')
print('Program is exiting.')
