# Helm Chart for sample-app-ci-cd

This Helm chart is designed to deploy sample-app-ci-cd on a Kubernetes cluster. It provides configuration options for various aspects of the deployment.

## Configuration

You can configure the deployment by modifying the values in the `values.yaml` file. Here's a breakdown of the available configuration options:

### Replica Count

The number of replicas to deploy:

```yaml
replicaCount: 1
```
### Docker Image

Configure the Docker image for your application. You can specify the image registry, repository path, image tag, and image pull policy:

```yaml
image:
  registry: docker.io
  repository: ""
  tag: ""
  pullPolicy: IfNotPresent
```

### Image Pull Secrets

If your Docker image requires authentication, you can provide image pull secrets:

```yaml
imagePullSecrets: []
```

### Helm Chart Overrides

You can override the Helm chart name and fullname if needed:

```yaml
nameOverride: ""
fullnameOverride: ""
```

### Annotations

Add annotations to the server deployment and pod:

```yaml
deploymentAnnotations: {}
podAnnotations: {}
```

### Pod Security Context

Configure the security context for the pod, including privilege escalation and user settings:

```yaml
securityContext:
  allowPrivilegeEscalation: false
  privileged: false
  readOnlyRootFilesystem: false
  runAsGroup: 1001
  runAsNonRoot: true
  runAsUser: 1001
```

### Service Configuration

Configure the Kubernetes service to expose the server. Specify the service type, port, and internal port:

```yaml
service:
  type: ClusterIP
  port: 8080
  internalPort: 80
```

### Ingress

If you want to expose the server using an Ingress resource, you can enable it and provide annotations and host settings:

```yaml
ingress:
  enabled: false
  annotations: {}
  hosts:
    - host: chart-example.local
      pathType: ImplementationSpecific
      paths: ["/"]
  tls: []
```

### Resources

Specify resource limits and requests for the server container:

```yaml
resources: {}
```

### Node Selector, Tolerations, and Affinity

Configure node selector, tolerations, and affinity settings for the pod:

```yaml
nodeSelector: {}
tolerations: []
affinity: {}
```

### Probe Configuration for Container Health

This Helm chart includes configurations for three types of probes to ensure the health and readiness of your containerized application: readiness probe, startup probe, and liveness probe.

## Readiness Probe Configuration

The readiness probe determines when your application is ready to accept traffic. Here are the key configurations:

- `failureThreshold`: The number of consecutive failures required to consider the container not ready.
- `initialDelaySeconds`: The initial delay before the probe is executed (in seconds).
- `periodSeconds`: How often the probe is performed (in seconds).
- `successThreshold`: The number of consecutive successes required to consider the container ready.
- `timeoutSeconds`: The maximum time for the probe to complete (in seconds).
- `path`: The path that the probe will access to determine readiness.

## Startup Probe Configuration

The startup probe checks if your container has started successfully. Here are the key configurations:

- `failureThreshold`: The number of consecutive failures required to consider the container not started successfully.
- `initialDelaySeconds`: The initial delay before the probe is executed (in seconds).
- `periodSeconds`: How often the probe is performed (in seconds).
- `successThreshold`: The number of consecutive successes required to consider the container started successfully.
- `timeoutSeconds`: The maximum time for the probe to complete (in seconds).
- `path`: The path that the probe will access during startup.

## Liveness Probe Configuration

The liveness probe determines if your container is still alive and healthy. Here are the key configurations:

- `failureThreshold`: The number of consecutive failures required to consider the container not live.
- `initialDelaySeconds`: The initial delay before the probe is executed (in seconds).
- `periodSeconds`: How often the probe is performed (in seconds).
- `successThreshold`: The number of consecutive successes required to consider the container live.
- `timeoutSeconds`: The maximum time for the probe to complete (in seconds).
- `path`: The path that the probe will access to determine liveness.

These probe configurations help ensure the reliability and stability of your containerized application. You can customize these values in your Helm chart's `values.yaml` file to meet your specific requirements.

### Pod Topology Spread

Define topology spread constraints for the pod:

```yaml
topologySpreadConstraints: []
```

### Extra Environment Variables

You can set additional environment variables for the server container:

```yaml
extraEnv: []
```

### Pod Disruption Budget

Enable a PodDisruptionBudget for the server pods (requires Kubernetes 1.21+):

```yaml
podDisruptionBudget:
  enabled: false
  minAvailable: 1
  maxUnavailable: ""
```

### Environment Variables

Configure environment variables for your application:

```yaml
env: []
```

For more information on Helm, please refer to the [Helm documentation](https://helm.sh/docs/).

### License

This project is licensed under the MIT License - see the LICENSE.md file for details.