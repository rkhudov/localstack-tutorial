import type {AWS} from '@serverless/typescript';

const serverlessConfiguration: AWS = {
  service: 'localstack-tutorial',
  frameworkVersion: '3',
  plugins: [
      'serverless-localstack',
      'serverless-python-requirements'
  ],
  provider: {
    name: 'aws',
    runtime: 'python3.8',
  },
  functions: {
    get: {
      handler: "src/functions/hello_world.handler",
      events: [
          {
            http: {
              path: 'hello-world',
              method: 'get',
              cors: true
            }
          }
      ]
    }
  },
  custom: {
    pythonRequirements: {
      dockerizePip: true,
    },
    localstack: {
      stages: 'local'
    }
  }
};

module.exports = serverlessConfiguration;
