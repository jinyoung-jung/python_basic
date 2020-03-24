{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Student(object):\n",
    "    def __init__(self, name, year, class_num, student_id):\n",
    "        self.name = name\n",
    "        self.year = year\n",
    "        self.class_num = class_num\n",
    "        self.student_id = student_id\n",
    "        \n",
    "    def introduce_myself(self):\n",
    "        return '{}, {}학년 {}반 {}번'.format(self.name, self.year, self.class_num, self.student_id)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
