{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c0db1745",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter first number:4\n",
      "Enter second number:2\n",
      "Enter your choise:\n",
      "1.Add\n",
      "2.Substract\n",
      "3.Multiply\n",
      "4.Divide\n",
      "3\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"Enter first number:\"))\n",
    "b=int(input(\"Enter second number:\"))\n",
    "ch=int(input(\"Enter your choise:\\n1.Add\\n2.Substract\\n3.Multiply\\n4.Divide\\n\"))\n",
    "if ch==1:\n",
    "    sum=a+b\n",
    "    print(sum)\n",
    "elif ch==2:\n",
    "    dif=a-b\n",
    "    print(dif)\n",
    "elif ch==3:\n",
    "    product=a*b\n",
    "    print(product)\n",
    "elif ch==4:\n",
    "    div=a%b\n",
    "    print(div)\n",
    "else:\n",
    "    print(\"Invalid Choise:\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b0e91948",
   "metadata": {},
   "outputs": [],
   "source": [
    "a=int(input(\"Enter first number:\"))\n",
    "b=int(input(\"Enter second number:\"))\n",
    "print(\"And:\",a and b)\n",
    "print(\"Or:\",a or b)\n",
    "print(\"Not:\",not b)\n",
    "print(\"a>b\",a>b)\n",
    "print(\"a<b\",a<b)\n",
    "print(\"a==b\",a==b)\n",
    "print(\"a>=b\",a>=b)\n",
    "print(\"a<=b\",a<=b)\n",
    "print(\"a!=b\",a!=b)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "64d7c917",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Merged: {'name': 'biya', 'age': 22, 'reg': 2026, 'place': 'kozhikode', 'college': 'AWH'}\n"
     ]
    }
   ],
   "source": [
    "dict1={'name':'biya','age':22,'reg':2026}\n",
    "dict2={'place':'kozhikode','college':'AWH',}\n",
    "dict1.update(dict2)\n",
    "print(\"Merged:\",dict1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "97a7784f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
