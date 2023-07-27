package mainpkg;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
@SpringBootApplication
public class SpringWebAndSvelteApplication {
	public static void main(String[] args) {
		SpringApplication.run(SpringWebAndSvelteApplication.class, args);
	}
    @Bean
    WebMvcConfigurer corsConfigurer() {
		return new WebMvcConfigurer() {
			@Override
			public void addCorsMappings(CorsRegistry registry) {
				registry
					.addMapping("/api/**")
					.allowedOriginPatterns("http://*.*")
					.allowedOrigins(
						"http://localhost:3000",
						"http://localhost:4000",
						"http://localhost:5000"
					)
					.allowedMethods("GET", "POST", "PUT", "DELETE")
					.allowedHeaders("Authorization", "Content-Type")
					.exposedHeaders("Custom-Header")
					.allowCredentials(true)
					.maxAge(3600);
			}
		};
	}
}