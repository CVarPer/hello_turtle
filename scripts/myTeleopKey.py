#!/usr/bin/env python

import rospy
import sys, select, termios, tty
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
from numpy import pi

# Función para leer la tecla presionada
def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

# Función para mover la tortuga
def movTortuga(key):
    if key == 'w':
        twist.linear.x = 1
    elif key == 's':
        twist.linear.x = -1
    elif key == 'd':
        twist.angular.z = -1
    elif key == 'a':
        twist.angular.z = 1
    elif key == 'r':
        Retorno()
    elif key == 'g':
        Giro180()
    else:
        pass
    pub.publish(twist)
    twist.linear.x = 0
    twist.angular.z = 0
    
# Función para resetear la posición de la tortuga
def Retorno():
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        teleport_abs = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        teleport_abs(5.54, 5.54, 0)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

# Función para rotar la tortuga 180 grados
def Giro180():
    rospy.wait_for_service('/turtle1/teleport_relative')
    try:
        teleport_rel = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
        teleport_rel(0, pi)
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    rospy.init_node('myTeleopKey')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
    twist = Twist()

    try:
        print("Control de la tortuga con las teclas. Presiona 'Ctrl + C' para salir.")
        while True:
            key = getKey()
            movTortuga(key)
    except rospy.ROSInterruptException:
        pass
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
