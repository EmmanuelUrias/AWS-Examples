## Filter event data from CLI
```sh
aws logs filter-log-events \
--log-group-name /example/basic/app \
--filter-pattern '{ $.method = "PUT" }'
```
## Create Metric Filter based on Method popularity and time
```sh
aws logs put-metric-filter \
--log-group-name "/example/basic/app" \
--filter-name "MethodPopularityByTimestamp" \
--filter-pattern '{ $.method = * && $.timestamp = * }' \
--metric-transformations metricName="PopularMethods",metricNamespace="AppMetrics",metricValue="1"
```
## Create a Metric Filter based on login attempts by IP
```sh
aws logs put-metric-filter \
--log-group-name "/example/basic/app" \
--filter-name "LoginAttemptsByIP" \
--filter-pattern '{ $.ip = * && $.method = "POST" && $.path = "/login" && $.timestamp = * }' \
--metric-transformations metricName="LoginAttempts",metricNamespace="AppMetrics",metricValue="1"

```
# Create a CloudWatch alarm for login attempts
```sh
aws cloudwatch put-metric-alarm \
--alarm-name "HighLoginAttempts" \
--metric-name "LoginAttempts" \
--namespace "AppMetrics" \
--statistic "Sum" \
--period 600 \
--threshold 3 \
--comparison-operator "GreaterThanThreshold" \
--evaluation-periods 1 
```