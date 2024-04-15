% Script para suscribirse al tópico de pose de turtle1

% Conectar a ROS
rosinit;

%% Crear un suscriptor para el tópico de pose
poseSub = rossubscriber('/turtle1/pose', 'turtlesim/Pose');

% Recibir el último mensaje de pose
latestPose = receive(poseSub, 1);

% Mostrar la información de la pose
disp('Última pose de turtle1:');
disp(latestPose);

%% Cerrar la conexión con ROS
rosshutdown;
