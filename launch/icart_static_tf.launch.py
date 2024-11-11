from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # launchの構成を示すLaunchDescription型の変数の定義
    ld = LaunchDescription()

    stfp_odom_basefootprint = Node(
            ## Configure the TF of the robot to the origin of the map coordinates
            package='tf2_ros',
            executable='static_transform_publisher',
            output='screen',
            arguments=['--x', '0', '--y', '0', '--z', '0',
                        '--qx', '0', '--qy', '0', '--qz', '0', '--qw', '1', 
                        '--frame-id', 'odom', '--child-frame-id', 'base_footprint']
    )

    stfp_basefootprint_baselink = Node(
            ## Configure the TF of the robot to the origin of the map coordinates
            package='tf2_ros',
            executable='static_transform_publisher',
            output='screen',
            arguments=['--x', '0', '--y', '0', '--z', '0',
                        '--qx', '0', '--qy', '0', '--qz', '0', '--qw', '1', 
                        '--frame-id', 'base_footprint', '--child-frame-id', 'base_link']
    )


    stfp_baselink_laser = Node(
        ## Configure the TF of the robot to the origin of the map coordinates
        package='tf2_ros',
        executable='static_transform_publisher',
        output='screen',
        arguments=['--x', '0', '--y', '0.22', '--z', '0',
                    '--qx', '0', '--qy', '0', '--qz', '0', '--qw', '1', 
                    '--frame-id', 'base_link', '--child-frame-id', 'laser']
    )

    stfp_map_odom = Node(
        ## Configure the TF of the robot to the origin of the map coordinates
        package='tf2_ros',
        executable='static_transform_publisher',
        output='screen',
        arguments=['--x', '0', '--y', '0', '--z', '0',
                    '--qx', '0', '--qy', '0', '--qz', '0', '--qw', '1', 
                    '--frame-id', 'map', '--child-frame-id', 'odom']
    )

    # LaunchDescriptionに、起動したいノードを追加する
    ld.add_action(stfp_map_odom)
    ld.add_action(stfp_odom_basefootprint)
    ld.add_action(stfp_basefootprint_baselink)
    ld.add_action(stfp_baselink_laser)

    # launch構成を返すようにする
    return ld