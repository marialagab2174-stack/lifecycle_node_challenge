# Challenge : Lifecycle Node (Managed Nodes) 🔄

Ce projet implémente un nœud à cycle de vie sous **ROS 2 Jazzy**. Contrairement aux nœuds classiques, les Lifecycle Nodes permettent un contrôle déterministe des états de fonctionnement (Configuration, Activation, Désactivation), ce qui est crucial pour la sécurité en robotique industrielle.

## 🏗 États de la Machine
- **Unconfigured** : Nœud instancié, ressources non allouées.
- **Inactive** : Ressources allouées mais aucun message n'est publié.
- **Active** : Nœud opérationnel (Publishing actif).

## 🛠 Compilation
```bash
cd ~/ros2_ws
colcon build --packages-select lifecycle_node_challenge
source install/setup.bash
```

## 🚀 Utilisation (Pilotage des transitions)
Lancer le nœud :
```bash
ros2 run lifecycle_node_challenge lc_node
```

Dans un autre terminal, changez les états manuellement :
```bash
# 1. Configurer
ros2 lifecycle set /my_lifecycle_node configure
# 2. Activer
ros2 lifecycle set /my_lifecycle_node activate
# 3. Désactiver
ros2 lifecycle set /my_lifecycle_node deactivate
```

---
**Développeur :** Maria Lagab  
**Spécialité :** Robotique et Système Intelligent
