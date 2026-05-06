# Challenge: ROS 2 Lifecycle Node 🔄

Ce projet implémente un **Managed Node** (nœud à cycle de vie) sous ROS 2 Jazzy. Contrairement aux nœuds classiques, les Lifecycle Nodes permettent de contrôler précisément le démarrage, la configuration et l'arrêt des composants d'un robot.

## 🏗 États de la Machine
- **Unconfigured** : Nœud instancié mais ressources non allouées.
- **Inactive** : Ressources allouées mais aucun message n'est publié.
- **Active** : Nœud opérationnel (Publishing/Subscriptions actifs).
- **Finalized** : Nœud détruit proprement.

## 🛠 Compilation
```bash
cd ~/ros2_ws
colcon build --packages-select lifecycle_node_challenge
source install/setup.bash
```

## 🚀 Utilisation (Transitions manuelles)
Lancer le nœud :
```bash
ros2 run lifecycle_node_challenge lc_node
```

Dans un autre terminal, piloter les transitions :
```bash
# Configurer
ros2 lifecycle set /my_lifecycle_node configure
# Activer
ros2 lifecycle set /my_lifecycle_node activate
# Désactiver
ros2 lifecycle set /my_lifecycle_node deactivate
```

---
**Maria Lagab** - Spécialité Robotique et Système Intelligent
