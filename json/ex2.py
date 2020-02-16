import json

json_data='''
{
    "kind": "APIGroupList",
    "apiVersion": "v1",
    "groups": [
        {
            "name": "apiregistration.k8s.io",
            "versions": [
                {
                    "groupVersion": "apiregistration.k8s.io/v1",
                    "version": "v1"
                },
                {
                    "groupVersion": "apiregistration.k8s.io/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "apiregistration.k8s.io/v1",
                "version": "v1"
            }
        },
        {
            "name": "extensions",
            "versions": [
                {
                    "groupVersion": "extensions/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "extensions/v1beta1",
                "version": "v1beta1"
            }
        },
        {
            "name": "apps",
            "versions": [
                {
                    "groupVersion": "apps/v1",
                    "version": "v1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "apps/v1",
                "version": "v1"
            }
        },
        {
            "name": "events.k8s.io",
            "versions": [
                {
                    "groupVersion": "events.k8s.io/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "events.k8s.io/v1beta1",
                "version": "v1beta1"
            }
        },
        {
            "name": "authentication.k8s.io",
            "versions": [
                {
                    "groupVersion": "authentication.k8s.io/v1",
                    "version": "v1"
                },
                {
                    "groupVersion": "authentication.k8s.io/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "authentication.k8s.io/v1",
                "version": "v1"
            }
        },
        {
            "name": "authorization.k8s.io",
            "versions": [
                {
                    "groupVersion": "authorization.k8s.io/v1",
                    "version": "v1"
                },
                {
                    "groupVersion": "authorization.k8s.io/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "authorization.k8s.io/v1",
                "version": "v1"
            }
        },
        {
            "name": "autoscaling",
            "versions": [
                {
                    "groupVersion": "autoscaling/v1",
                    "version": "v1"
                },
                {
                    "groupVersion": "autoscaling/v2beta1",
                    "version": "v2beta1"
                },
                {
                    "groupVersion": "autoscaling/v2beta2",
                    "version": "v2beta2"
                }
            ],
            "preferredVersion": {
                "groupVersion": "autoscaling/v1",
                "version": "v1"
            }
        },
        {
            "name": "batch",
            "versions": [
                {
                    "groupVersion": "batch/v1",
                    "version": "v1"
                },
                {
                    "groupVersion": "batch/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "batch/v1",
                "version": "v1"
            }
        },
        {
            "name": "certificates.k8s.io",
            "versions": [
                {
                    "groupVersion": "certificates.k8s.io/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "certificates.k8s.io/v1beta1",
                "version": "v1beta1"
            }
        },
        {
            "name": "networking.k8s.io",
            "versions": [
                {
                    "groupVersion": "networking.k8s.io/v1",
                    "version": "v1"
                },
                {
                    "groupVersion": "networking.k8s.io/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "networking.k8s.io/v1",
                "version": "v1"
            }
        },
        {
            "name": "policy",
            "versions": [
                {
                    "groupVersion": "policy/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "policy/v1beta1",
                "version": "v1beta1"
            }
        },
        {
            "name": "rbac.authorization.k8s.io",
            "versions": [
                {
                    "groupVersion": "rbac.authorization.k8s.io/v1",
                    "version": "v1"
                },
                {
                    "groupVersion": "rbac.authorization.k8s.io/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "rbac.authorization.k8s.io/v1",
                "version": "v1"
            }
        },
        {
            "name": "storage.k8s.io",
            "versions": [
                {
                    "groupVersion": "storage.k8s.io/v1",
                    "version": "v1"
                },
                {
                    "groupVersion": "storage.k8s.io/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "storage.k8s.io/v1",
                "version": "v1"
            }
        },
        {
            "name": "admissionregistration.k8s.io",
            "versions": [
                {
                    "groupVersion": "admissionregistration.k8s.io/v1",
                    "version": "v1"
                },
                {
                    "groupVersion": "admissionregistration.k8s.io/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "admissionregistration.k8s.io/v1",
                "version": "v1"
            }
        },
        {
            "name": "apiextensions.k8s.io",
            "versions": [
                {
                    "groupVersion": "apiextensions.k8s.io/v1",
                    "version": "v1"
                },
                {
                    "groupVersion": "apiextensions.k8s.io/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "apiextensions.k8s.io/v1",
                "version": "v1"
            }
        },
        {
            "name": "scheduling.k8s.io",
            "versions": [
                {
                    "groupVersion": "scheduling.k8s.io/v1",
                    "version": "v1"
                },
                {
                    "groupVersion": "scheduling.k8s.io/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "scheduling.k8s.io/v1",
                "version": "v1"
            }
        },
        {
            "name": "coordination.k8s.io",
            "versions": [
                {
                    "groupVersion": "coordination.k8s.io/v1",
                    "version": "v1"
                },
                {
                    "groupVersion": "coordination.k8s.io/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "coordination.k8s.io/v1",
                "version": "v1"
            }
        },
        {
            "name": "node.k8s.io",
            "versions": [
                {
                    "groupVersion": "node.k8s.io/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "node.k8s.io/v1beta1",
                "version": "v1beta1"
            }
        },
        {
            "name": "discovery.k8s.io",
            "versions": [
                {
                    "groupVersion": "discovery.k8s.io/v1beta1",
                    "version": "v1beta1"
                }
            ],
            "preferredVersion": {
                "groupVersion": "discovery.k8s.io/v1beta1",
                "version": "v1beta1"
            }
        }
    ]
}
'''
data=json.loads(json_data) 
#print(type(data))
#print(type(data['groups']))
for value in data['groups']:
   # print(type(value))
    print(value['name'])
    for groupv in (value['versions']):
        #print(type(groupv))
         del(groupv['groupVersion'])
new_string=json.dumps(data)
print(new_string)


