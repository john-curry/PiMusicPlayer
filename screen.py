import time
import random as rand
import Adafruit_CharLCD as LCD

class my_screen:
  indeces = [ 1, 424 ,818, 1225, 1574, 1848, 2261, 2548, 2902, 3329, 3679, 3898, 4249, 4250, 4428, 4429, 4430, 4431, 4432, 4433, 4450, 4451, 4535 ]

  # Raspberry Pi pin configuration:
  lcd_en        = 14
  lcd_rs        = 15
  lcd_d4        = 21
  lcd_d5        = 20
  lcd_d6        = 16
  lcd_d7        = 12
  lcd_backlight =  4

  # Define LCD column and row size for 16x2 LCD.
  lcd_columns = 16
  lcd_rows    = 2
  lcd_length  = lcd_rows * lcd_columns

  book = (open("/var/books/book.txt")).read()
  start = indeces[rand.randint(0, len(indeces))]

  lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                             lcd_columns, lcd_rows, lcd_backlight)

  def message(self, output):
    self.lcd.clear()
    self.lcd.message(output)

  def sleep(self):
    sleep = 2.5
    time.sleep(sleep)

  #while True:
  #  for i in range(start, int(len(book)/16)):
  #    lcd.clear()
  #    index = i*16
  #    #print book[index:index + 16]
  #    lcd.message(book[index:index + 16])
  #    sleep()
