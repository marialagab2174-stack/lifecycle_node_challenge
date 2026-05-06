import rclpy
from rclpy.lifecycle import Node, State, TransitionCallbackReturn
from std_msgs.msg import String

class MyLifecycleNode(Node):
    def __init__(self, node_name):
        super().__init__(node_name)
        self.pub = None
        self.timer = None

    def on_configure(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info('Configuration du nœud : Initialisation des ressources...')
        return TransitionCallbackReturn.SUCCESS

    def on_activate(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info('Activation : Création du publisher et du timer...')
        self.pub = self.create_lifecycle_publisher(String, 'lifecycle_topic', 10)
        self.timer = self.create_timer(1.0, self.publish_msg)
        return super().on_activate(state)

    def on_deactivate(self, state: State) -> TransitionCallbackReturn:
        self.get_logger().info('Désactivation : Arrêt des flux de données...')
        if self.timer:
            self.destroy_timer(self.timer)
        self.pub = None 
        return super().on_deactivate(state)

    def publish_msg(self):
        if self.pub is not None and self.pub.is_activated:
            msg = String()
            msg.data = 'Nœud Actif : Transmission en cours...'
            self.pub.publish(msg)
            self.get_logger().info('Message publié sur /lifecycle_topic')

def main(args=None):
    rclpy.init(args=args)
    node = MyLifecycleNode('my_lifecycle_node')
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
