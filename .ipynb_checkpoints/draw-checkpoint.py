{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9be6c0d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def draw_vector(V):\n",
    "    \"\"\"The function takes the following  input:\n",
    "    V = [v_x,v_y,v_z], a list of the x,y & z components of a vector V of non-zero length\n",
    "    and it creates a canvas representing the vector in green and the relative unit vector in red\n",
    "    Both vectors have the tail in the center of the canvas, at position (0,0,0)\"\"\"\n",
    "    scene = canvas()\n",
    "    Varrow = arrow(pos = vector(0,0,0), axis = vector(V[0], V[1],V[2]), shaftwidth = 0.05, color = color.green)\n",
    "    u = unit_vector(V)  # Call the function unit_vector on the instance vector V\n",
    "    uarrow = arrow(pos = vector(0,0,0), axis = vector(u[0], u[1],u[2]), shaftwidth=0.07, color = color.red)"
   ]
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
