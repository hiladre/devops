resource "helm_release" "nginx_ingress" {
  name       = "nginx-ingress"
  namespace  = "app-namespace"
  chart      = "ingress-nginx"
  repository = "https://kubernetes.github.io/ingress-nginx"
}
