import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    # NOTE: For this test, we are not using any of our custom files.

    # =================================================================
    # == VITAL TEST: Launching the new Gazebo with NO world file     ==
    # == This will test if the 'gz sim' command itself is working.   ==
    # =================================================================
    gazebo = ExecuteProcess(
        # NOTE: We launch 'gz sim -r' with no world file argument.
        # It should open a default empty world.
        cmd=['gz', 'sim', '-r'],
        output='screen'
    )
    # =================================================================

    # All other nodes are disabled for this test to isolate the problem.
    # bridge = Node(...)
    # node_robot_state_publisher = Node(...)
    # spawn_entity = Node(...)

    return LaunchDescription([
        gazebo,
    ])