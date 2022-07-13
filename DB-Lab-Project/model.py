from neo4j import GraphDatabase
import logging

class App:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        
    def close(self):
        self.driver.close()

    def find_student_score(self, student_name):
        with self.driver.session() as session:
            result = session.read_transaction(self._find_and_return_student, student_name)
            print(result)
            for row in result:
                print("Student Score: {row}".format(row=row))
            return result[0] if len(result) else -1

    @staticmethod
    def _find_and_return_student(tx, student_name):
        query = (
            "MATCH (p:Student) "
            "WHERE p.Name = $student_name "
            "RETURN p.Score AS Score"
        )
        result = tx.run(query, student_name=student_name)
        print(result)
        return [row["Score"] for row in result]


    def add_student_to_section(self, student_name, section_name):
        with self.driver.session() as session:
            result = session.write_transaction(
                self._add_student_to_section, student_name, section_name)

    @staticmethod
    def _add_student_to_section(tx, student_name, section_name):
        query = (
            "MATCH (s1:Student) where s1.Name=$student_name MATCH (e1:Section) where e1.Class_Name=$section_name CREATE (s1)-[:STUDENT_OF]->(e1)"
        )
        result = tx.run(query, student_name=student_name, section_name=section_name)
        try:
            return
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise

    def new_student(self, student_name, student_score, student_year):
        with self.driver.session() as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.write_transaction(
                self._new_student, student_name, student_score, student_year)

    @staticmethod
    def _new_student(tx, student_name, student_score, student_year):
        query = (
            "CREATE (s:Student {Name:$student_name, Score:$student_score, Year:$student_year})"
        )
        result = tx.run(query, student_name=student_name, student_score=student_score,student_year=student_year)
        try:
            return
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise
        
    def update_student_score(self, student_name, student_score):
        with self.driver.session() as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.write_transaction(
                self._update_student_score, student_name, student_score)

    @staticmethod
    def _update_student_score(tx, student_name, student_score):
        query = (
            "MATCH (n:Student {Name:$student_name}) SET n.Score =$student_score"
        )
        result = tx.run(query, student_name=student_name, student_score=student_score)
        try:
            return
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise
        
    def delete_student(self, student_name):
        with self.driver.session() as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.write_transaction(
                self._delete_student, student_name)

    @staticmethod
    def _delete_student(tx, student_name):
        query = (
            "MATCH (n:Student {Name:$student_name}) DELETE n"
        )
        result = tx.run(query, student_name=student_name)
        try:
            return
        # Capture any errors along with the query and data for traceability
        except ServiceUnavailable as exception:
            logging.error("{query} raised an error: \n {exception}".format(
                query=query, exception=exception))
            raise

if __name__ == "__main__":
    # Aura queries use an encrypted connection using the "neo4j+s" URI scheme
    uri = "neo4j+s://b668c99d.databases.neo4j.io"
    user = "neo4j"
    password = "PVSTqrQ9e29sU01mus2qgOfOQNxFKa2fSL69EC3gsnU"
    app = App(uri, user, password)
    #Here we work with Database
    #app.find_student_score("Reza")
    # app.add_student_to_section("Alireza", "Algohritm_02")
    #app.new_student("Homayoon", 19, 97)
    app.update_student_score("Millad", 15)
    # app.delete_student("Homayoon")
    app.close()