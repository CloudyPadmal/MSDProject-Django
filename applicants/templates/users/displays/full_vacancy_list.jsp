<%@ include file="/WEB-INF/jsp/head.jsp"%>
<body>
	<nav class="navbar navbar-inverse navbar-fixed-top">
		<div class="container-fluid">
			<div class="navbar-header">
				<a class="navbar-brand">All Vacancies</a>
			</div>
			<div id="navbar" class="navbar-collapse collapse">
				<ul class="nav navbar-nav navbar-right">
					<li><form:form action="view_requests" method="POST">
							<button type="submit" name="edit" value="edit" class="edit">Requests</button>
						</form:form></li>
					<li><form:form action="/logout" method="POST">
							<button type="submit" name="edit" value="edit" class="edit">Logout</button>
						</form:form></li>
				</ul>
			</div>
		</div>
	</nav>
	<div class="vacancy-list">
		<br />
		<c:if test="${not empty msg}">
			<div class="alert alert-${css} alert-dismissible" role="alert">
				<button type="button" class="close" data-dismiss="alert"
					aria-label="Close">
					<span aria-hidden="true">&times;</span>
				</button>
				<strong>${msg}</strong>
			</div>
		</c:if>

		<table class="table table-striped">
			<thead>
				<tr>
					<th>#</th>
					<th>Title</th>
					<th>Salary</th>
					<th>Description</th>
					<th>Applicant</th>
					<th>Preferences</th>
					<th>Action</th>
				</tr>
			</thead>

			<c:forEach var="vacancy" items="${vacancies}">
				<tr>
					<td>${vacancy.id}</td>
					<td>${vacancy.title}</td>
					<td>${vacancy.salary}</td>
					<td id="description">${vacancy.description_1}&nbsp;${vacancy.description_2}</td>
					<td><c:if test="${vacancy.open}">
							<c:choose>
								<c:when test="${vacancy.awarded}">
									<button type="button" class="btn btn-awarded disabled"
										data-toggle="dropdown">${vacancy.applicant}</button>
								</c:when>
								<c:otherwise>
									<div class="btn-group">
										<button type="button" class="btn btn-success dropdown-toggle"
											data-toggle="dropdown">${vacancy.applicant}</button>
										<ul class="dropdown-menu" role="menu">
											<li><form type="submit"
													action="vacancy/accept/${vacancy.id}" method="POST">
													<button class="btn btn-primary">Approve</button>
												</form></li>
											<li><form type="submit"
													action="vacancy/reject/${vacancy.id}" method="POST">
													<button class="btn btn-warning">Reject</button>
												</form></li>
											<li><form type="submit"
													action="user/view/${vacancy.applicant}" method="POST">
													<button class="btn btn-warning">Show!</button>
												</form></li>
										</ul>
									</div>
								</c:otherwise>
							</c:choose>
						</c:if></td>
					<td><c:forEach var="preference" items="${vacancy.preferences}">
							<li>${preference}</li>
						</c:forEach></td>
					<td id="buttons">
						<form type="submit" action="vacancy/delete/${vacancy.id}"
							method="POST">
							<button class="btn btn-danger">Delete</button>
						</form>
					</td>
				</tr>
			</c:forEach>
		</table>
	</div>
</body>
<!-- � Padmal -->
