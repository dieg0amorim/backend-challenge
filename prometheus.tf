resource "aws_cloudwatch_log_group" "prometheus_logs" {
  name              = "/ecs/prometheus"
  retention_in_days = 7
}

resource "aws_ecs_task_definition" "prometheus" {
  family                   = "my-task-prometheus"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = aws_iam_role.ecs_execution_role.arn
  cpu = "512"  # 2 vCPUs
  memory = "4096"  # 4GB de memória
  depends_on = [ aws_cloudwatch_log_group.example ]

  container_definitions = <<EOF
[
  {
    "name": "my-container",
    "image": "devdihdca/prometheus:latest",
    "portMappings": [
      {
        "containerPort":9090,
        "hostPort": 9090
      }
    ],
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "/ecs/prometheus",
        "awslogs-region": "us-east-1",
        "awslogs-stream-prefix": "prometheus"
      }
    }
  }
]  
EOF
}


resource "aws_ecs_service" "prometheus_service" {
  name            = "prometheus-service"
  cluster         = aws_ecs_cluster.my_cluster.id
  task_definition = aws_ecs_task_definition.prometheus.arn
  launch_type     = "FARGATE"
#  desired_count = 1

  network_configuration {
    subnets = [aws_subnet.public_subnet.id]
    security_groups = [aws_security_group.security_group.id]
    assign_public_ip = true
   
  }
}
