% Script para enviar valores asociados a la pose de turtle1

% Conectar a ROS
rosinit;

%% Crear un publicador para el tópico de comandos de velocidad
velPub = rospublisher('/turtle1/cmd_vel', 'geometry_msgs/Twist');

% Crear un mensaje de velocidad
velMsg = rosmessage(velPub);

% Asignar valores de velocidad lineal y angular (ejemplo)
velMsg.Linear.X = 1;
velMsg.Angular.Z = 0.5;

% Enviar el mensaje de velocidad
send(velPub, velMsg);

% Esperar un tiempo (ejemplo)
pause(1);

%% Cerrar la conexión con ROS
rosshutdown;