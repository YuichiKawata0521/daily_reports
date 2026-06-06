# 注意点

- 名詞と動詞をセットで書き出す
- ドメインで切り分けてエンティティの抽出を行う
- エンティティ or 値オブジェクトかを意識する


# フェーズ1 エンティティ抽出

## CustomUser
- id
- employeeNo

- firstName(AbstractUserに含まれる)
- middleName
- lastName(AbstractUserに含まれる)
- sex
- birth_date
- email(AbstractUserに含まれる)
- tel

- password(AbstractUserに含まれる)
- role

- postcode
- prefecture
- city
- address1
- address2

- department

- createdAt
- updatedAt
- isActive(AbstractUserに含まれる)

## departments (自己参照)
- id
- name
- parentId (departments.id)
- createdAt
- updatedAt
- isActive
## roles
- id
- role
- createdAt
- UpdatedAt
- isActive

## daily_reports
- id
- userId
- title
- content
- createdAt
- updatedAt
- status(textchoice)

## weekly_reports
- id
- userId
- title
- content
- createdAt
- updatedAt
- status(textchoice)

## tags
- id
- name
- createdAt

## report_tags
- reportId
- tagId

## templates
- id
- departmentId
- contentLayout
- createdAt
- updatedAt
- isActive