import random

from locust import HttpLocust, TaskSet, task


class UserBehaviour(TaskSet):

    @task(3)
    def index(self):
        self.client.get('/')

    @task(2)
    def get_parts(self):
        self.client.get("/parts")

    @task(1)
    def get_parts_detail(self):
        self.client.get("/parts/{}".format(random.randrange(100),
                                           name="/parts/[id]"))


class WebsiteUser(HttpLocust):
    task_set = UserBehaviour
    min_wait = 5000
    max_wait = 9000
