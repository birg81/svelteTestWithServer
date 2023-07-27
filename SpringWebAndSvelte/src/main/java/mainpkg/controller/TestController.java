package mainpkg.controller;
import java.util.ArrayList;
import java.util.HashMap;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@RestController
@RequestMapping("/api/people")
public class TestController {
	private ArrayList<HashMap<String,String>> people = new ArrayList<>();
	public TestController() {
		HashMap<String, String> person = null;
		person = new HashMap<>();
		person.put("firstname", "Antonio");
		person.put("lastname", "Esposito");
		person.put("gender", "male");
		people.add(person);
		person = new HashMap<>();
		person.put("firstname", "Biagio");
		person.put("lastname", "Greco");
		person.put("gender", "male");
		people.add(person);
		person = new HashMap<>();
		person.put("firstname", "Carlo");
		person.put("lastname", "De Rosa");
		person.put("gender", "male");
		people.add(person);
		person = new HashMap<>();
		person.put("firstname", "Davide");
		person.put("lastname", "Sansone");
		person.put("gender", "male");
		people.add(person);
	}
	@GetMapping
	public ArrayList<HashMap<String, String>> getPeople() {
		return people;
	}
	@GetMapping("/{id}")
	public HashMap<String, String> getPerson(@PathVariable int id) {
		return people.get(id);
	}
}