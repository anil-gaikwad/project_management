

class AdminRoutes:
    TAGS = ["Admin"]
    ADMIN = "admin"


class ProjectRoutes:
    TAGS = ["Project"]
    PROJECT = "project"
    BASE_PROJECT = f"/{PROJECT}"
    DELETE_PROJECT = f"/{PROJECT}/{{project_id}}"
    UPDATE_PROJECT = f"/{PROJECT}/{{project_id}}"
    GET_PROJECT = f"/{PROJECT}/{{project_id}}"
    ADD_COMMENT = f"/{PROJECT}/{{project_id}}/comment"


class EmployeeRoutes:
    TAGS = ["Employee"]
    EMPLOYEE = "employee"
    BASE_EMPLOYEE = f"/{EMPLOYEE}"
    DELETE_EMPLOYEE = f"/{EMPLOYEE}/{{employee_id}}"
    UPDATE_EMPLOYEE = f"/{EMPLOYEE}/{{employee_id}}"


class CompanyRoutes:
    TAGS = ["Company"]
    COMPANY = "company"
    BASE_COMPANY = f"/{COMPANY}"
    DELETE_COMPANY = f"/{COMPANY}/{{company_id}}"
    GET_COMPANY = f"/{COMPANY}/{{company_id}}"


class CommentRoutes:
    TAGS = ["Comment"]
    COMMENT = "comment"
    BASE_COMMENT = f"/{COMMENT}"
    DELETE_COMMENT = f"/{COMMENT}/{{comment_id}}"
    WEBSOCKET = f"/{COMMENT}/{{project_id}}"
