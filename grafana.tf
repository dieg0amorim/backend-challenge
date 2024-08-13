resource "aws_cloudwatch_log_group" "grafana_logs" {
  name              = "/ecs/grafana"
  retention_in_days = 7
}

resource "aws_ecs_task_definition" "grafana" {
  family                   = "my-task-grafana"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn       = aws_iam_role.ecs_execution_role.arn
  cpu = "512"  
  memory = "4096"
  depends_on = [ aws_cloudwatch_log_group.example ]

  container_definitions = <<EOF
[
  {
    "name": "my-container",
    "image": "grafana/grafana:latest",
    "portMappings": [
      {
        "containerPort":3000,
        "hostPort": 3000
      }
    ],
    "logConfiguration": {
      "logDriver": "awslogs",
      "options": {
        "awslogs-group": "/ecs/grafana",
        "awslogs-region": "us-east-1",
        "awslogs-stream-prefix": "grafana"
      }
    }
  }
]  
EOF
}


resource "aws_ecs_service" "grafana_service" {
  name            = "grafana-service"
  cluster         = aws_ecs_cluster.my_cluster.id
  task_definition = aws_ecs_task_definition.grafana.arn
  launch_type     = "FARGATE"
#  desired_count = 1

  network_configuration {
    subnets = [aws_subnet.public_subnet.id]
    security_groups = [aws_security_group.security_group.id]
    assign_public_ip = true
   
  }
}
