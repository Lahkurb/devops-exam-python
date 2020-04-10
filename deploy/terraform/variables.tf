variable "cluster-name"{
    default ="exam-cluster"
}
variable "cluster-description"{
    default ="Cluster k8 to task 1"
}
variable "project"{
    default ="exam-devops"
}
variable "region"{
    default ="us-central1"
}
variable "zone"{
    default ="us-central1-c"
}
variable "node_count"{
    default =1
}
variable "machine_type"{
    default ="n1-standard-1"
}